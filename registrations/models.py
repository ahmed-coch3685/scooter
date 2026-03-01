from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = CloudinaryField('image',blank=True, null=True)
    REQUIRED_FIELDS = ['email']

