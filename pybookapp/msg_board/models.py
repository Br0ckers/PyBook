from django.db import models
# from django.db.models import forms



# # Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user_message = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
