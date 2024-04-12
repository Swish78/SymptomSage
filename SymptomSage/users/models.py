from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255, null=False, blank=False)
    dob = models.DateField(null=False, blank=False, default=timezone.now)
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']
