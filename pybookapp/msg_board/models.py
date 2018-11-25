#from django.db import models
from djongo import models
from django.utils import timezone

class Message(models.Model):
    text = models.TextField(max_length=200)
    date = models.DateField(null=True, default = timezone.localtime())
    like_count = models.IntegerField(default=0)
    #meta_data = models.EmbeddedModelField(model_container=MetaData)
    objects = models.DjongoManager()

    def __str__(self):
        return self.text

    def increment_like(self):
        self.like_count = self.like_count + 1

class Player(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=15, default='password')
    last_login = models.DateField(null=True, default = '2018-01-01')
    last_ipaddress = models.CharField(max_length=20, null=True)
    message_list = models.ArrayReferenceField(to=Message, null=True, blank=True)
    #messagelist = models.ArrayReferenceField(to=Message, on_delete = models.CASCADE)
    objects = models.DjongoManager()

    def __str__(self):
        return self.user_name

# class MetaData(models.Model):
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     class Meta:
#         abstract = True
