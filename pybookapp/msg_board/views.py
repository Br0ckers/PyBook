from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.generic import TemplateView
from msg_board.models import Player,Message
from pymongo import MongoClient
import urllib.parse

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['user_name', 'email', 'password', 'last_login', 'last_ipaddress','message_list']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'date', 'like_count']

class UserListView(TemplateView):
    def get(self, request, **kwargs):
        data = {}
        data["user_name"] = "Travolta"
        data["email"] = "Travolta@gmail.com"
        data["user_message"] = "Its cold in here"
        return render(request, 'user.html', {"data": data})

class UserListProperView(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching users via Djongo")
        player = Player.objects.all()
        print(player)
        data = {}
        data['object_list'] = player
        return render(request, 'player.html', {"data": data})


class UserListProperView1(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching users using PyMongo")
        client = MongoClient(port=27017)
        db = client.pybook_test1
        result = db.dummyplayer.find()
        print(result)
        data = {}
        data['object_list'] = result
        return render(request, 'player.html', {"data": data})
