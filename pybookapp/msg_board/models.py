#from django.db import models
from djongo import models
from django.utils import timezone
from django.conf import  settings
from django.contrib.auth.models import User

class Message(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(class)s_username', )
    text = models.TextField(max_length=200)
    date = models.DateField(null=True, default = timezone.now)
    like_count = models.IntegerField(default=0)
    objects = models.DjongoManager()

    def __str__(self):
        return self.text

    def increment_like(self):
        self.like_count = self.like_count + 1

    def get_absolute_url(self):
        return reverse('message_detail', kwargs={'pk': self.pk})

class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    nickname = models.CharField(max_length=30)
    last_ipaddress = models.CharField(max_length=20, null=True)
    friend_list = models.ArrayReferenceField(to='self', null=True, blank=True, on_delete=models.CASCADE)
    objects = models.DjongoManager()

    def __str__(self):
        return self.nickname
    
    

    def get_absolute_url(self):
        return reverse('member_detail', kwargs={'pk': self.pk})
