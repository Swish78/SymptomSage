from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.decorators import login_required
from .models import Blog, BlogReview
from .serializers import BlogSerializer, BlogReviewSerializer
import jwt, datetime
from django.conf import settings
from django.contrib.auth.models import User


class BlogListAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = BlogSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(author=request.user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    def post(self, request):
        # Get the 'Authorization' header from request headers
        auth_header = request.headers.get('Authorization', '')

        # Check if the 'Authorization' header is present
        if auth_header:
            # Split the header value to extract the token
            token_parts = auth_header.split(' ')
            if len(token_parts) == 2:
                token = token_parts[1]
                try:
                    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                    user_id = payload['user_id']
                    # Retrieve user object based on user ID
                    user = User.objects.get(pk=user_id)
                except jwt.ExpiredSignatureError:
                    raise AuthenticationFailed('Token has expired')
                except jwt.InvalidTokenError:
                    raise AuthenticationFailed('Invalid token')
                except User.DoesNotExist:
                    raise AuthenticationFailed('User does not exist')

                # Assign the user as the author of the blog
                request.data['author'] = user.id

                # Now you can proceed with creating the blog
                serializer = BlogSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(author=user)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise AuthenticationFailed('Invalid Authorization header format')
        else:
            raise AuthenticationFailed('Authorization header is missing')


class BlogDetailAPIView(APIView):
    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogReviewListCreateAPIView(APIView):
    def get(self, request):
        blog_reviews = BlogReview.objects.all()
        serializer = BlogReviewSerializer(blog_reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Decode JWT token to obtain user ID
        token = request.headers.get('Authorization', '').split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            # Retrieve user object based on user ID
            user = User.objects.get(pk=user_id)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        except User.DoesNotExist:
            raise AuthenticationFailed('User does not exist')

        # Assign the user as the reviewer of the review
        request.data['reviewer'] = user.id

        # Now you can proceed with creating the review
        serializer = BlogReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(reviewer=user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BlogReviewDetailAPIView(APIView):
    def get(self, request, pk):
        blog_review = BlogReview.objects.get(pk=pk)
        serializer = BlogReviewSerializer(blog_review)
        return Response(serializer.data)

    def put(self, request, pk):
        blog_review = BlogReview.objects.get(pk=pk)
        serializer = BlogReviewSerializer(blog_review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


