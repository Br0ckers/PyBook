#from django.db import models
from djongo import models
from django import forms


# # Create your models here.


class Message(models.Model):
    text = models.TextField(max_length=200)
    date = models.DateField()
    like_count = models.IntegerField(default=0)
    objects = models.DjongoManager()

    def __str__(self):
        return self.text


class Player(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15, default='password')
    last_login = models.DateField(null=True, default = '2018-01-01')
    last_ipaddress = models.CharField(max_length=20, blank=True)
    message_list = models.ArrayReferenceField(to=Message, null=True, default = '')
    #messagelist = models.ArrayReferenceField(to=Message, on_delete = models.CASCADE)
    objects = models.DjongoManager()

    def __str__(self):
        return self.user_name
