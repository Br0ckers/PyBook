#from django.db import models
from djongo import models
from django.utils import timezone
from django.conf import  settings
from django.contrib.auth.models import User

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

class Message(models.Model):
    text = models.TextField(max_length=200)
    date = models.DateField(null=True, default = timezone.now)
    like_count = models.IntegerField(default=0)
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    objects = models.DjongoManager()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        return reverse('message_detail', kwargs={'pk': self.pk})
