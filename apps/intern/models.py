from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=128)  # Add a password field

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
