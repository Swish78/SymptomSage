from django.contrib.auth.decorators import login_required
from rest_framework import status, response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.contrib.auth import logout
from users.serializers import UserSerializer
from users.models import User
import jwt, datetime

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found. Please register first.')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password. Please check your username and password.')

        # Generate JWT token
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response({'token': token}, status=status.HTTP_202_ACCEPTED)

        response.set_cookie('jwt_token', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        # Return token in the response
        return response


# @login_required()
class LogoutView(APIView):
    def post(self, request):
        # Clear the JWT token cookie
        response = Response()
        response.delete_cookie('jwt_token')
        response.data = {'message': 'Logged out.'}  # Correct assignment of data
        return response


class ProfileView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt_token')

        if not token:
            raise AuthenticationFailed('User not found. Please register first.')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized. Please login first.')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)