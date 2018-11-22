#from django.db import models
from djongo import models
from django import forms


# # Create your models here.
class Player(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user_message = models.CharField(max_length=100)
    objects = models.DjongoManager()

    def __str__(self):
        return self.user_name
