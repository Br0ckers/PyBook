#from django.db import models
from djongo import models
from django.utils import timezone

class Message(models.Model):
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
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=15, default='password')
    last_login = models.DateField(null=True, default = '2018-01-01')
    last_ipaddress = models.CharField(max_length=20, null=True)
    #message_list = models.ArrayReferenceField(to=Message, null=True, blank=True, on_delete = models.CASCADE)
    friend_list = models.ArrayReferenceField(to='self', null=True, blank=True, on_delete = models.CASCADE)
    objects = models.DjongoManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('member_detail', kwargs={'pk': self.pk})


class Message(models.Model):
    text = models.TextField(max_length=200)
    date = models.DateField(null=True, default = timezone.now())
    like_count = models.IntegerField(default=0)
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    objects = models.DjongoManager()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        return reverse('message_detail', kwargs={'pk': self.pk})
