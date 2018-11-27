from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'date', 'like_count']

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'password']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
