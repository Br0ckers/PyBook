from django.contrib import admin
from .models import Player
from .models import Message

admin.site.register([Player,Message])
# Register your models here.
