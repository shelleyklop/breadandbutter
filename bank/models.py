from django.db import models

from django.contrib.auth.models import User


class User_type(models.Model):
    type_name = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User)
    user_type = models.ForeignKey(User_type)	