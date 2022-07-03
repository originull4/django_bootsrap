from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


def avatar_upload(instance, filename):
    # get file extension
    ext = filename.split('.')[-1]
    # Returns the new name in lowercase and slugified
    return f'avatars/{slugify(str(instance.username).lower())}.{ext}'


class Account(AbstractUser):
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'))

    gender = models.CharField(max_length=6, blank=False, choices=GENDER_CHOICES)
    avatar = models.ImageField(upload_to=avatar_upload, default='avatars/default.png')


    def __str__(self):
        return self.username