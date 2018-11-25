from django.contrib import admin
from .models import Member
from .models import Message

admin.site.register([Member,Message])
# Register your models here.
