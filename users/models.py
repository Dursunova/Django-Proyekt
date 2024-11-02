from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# User = get_user_model()
    
class CustomUser(AbstractUser):
    bio = models.TextField( blank=True, null=True)