from django.contrib import admin
from .models import Member
from .models import Message
from django.contrib.auth.models import User


admin.site.register([Member,Message])
# Register your models here.
# admin.site.unregister(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ( 'username', 'id')
#    # list_filter = ('status', 'due_back')
    
#     fieldsets = (
#         (None, {
#             'fields': ('password','last_login', 'is_superuser','is_staff','is_active')
#         }),
#         ('Availability', {
#             'fields': ('id', 'username')
#         }),
#     )
