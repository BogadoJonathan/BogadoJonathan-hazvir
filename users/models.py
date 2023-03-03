from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    facebook = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self) -> str:
        return self.username

