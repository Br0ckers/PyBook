from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.generic import TemplateView
from msg_board.models import Player
from pymongo import MongoClient
import urllib.parse

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'msg_board/index.html', context=None)

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['user_name', 'email', 'user_message']

class UserListView(TemplateView):
    def get(self, request, **kwargs):
        data = {}
        data["user_name"] = "Travolta"
        data["email"] = "Travolta@gmail.com"
        data["user_message"] = "Its cold in here"
        return render(request, 'msg_board/user.html', {"data": data})

class UserListProperView(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching users via Djongo")
        player = Player.objects.all()
        print(player)
        print(len(player))
        print(dir(player))
        data = {}
        data['object_list'] = player
        return render(request, 'msg_board/player.html', {"data": data})


class UserListProperView1(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching users using PyMongo")
        client = MongoClient(port=27017)
        print(client)
        db = client.pybook_test1
        print(db)
        result = db.dummyplayer.find()
        print(result)
        data = {}
        data['object_list'] = result
        return render(request, 'msg_board/player.html', {"data": data})

messages = [
    {
        'user_name': 'Fred Bloggs',
        'title': 'Message One',
        'user_message': 'Hello, I am creating a pybook app',
        'date_posted': '22 November, 2018'
    },
    {
        'user_name': 'Frank Skinner',
        'title': 'Message Two',
        'user_message': 'Hello, this is another message',
        'date_posted': '23 November, 2018'
    }

]
def home(request):
    context = {
        'messages': messages
    }
    return render(request, 'msg_board/home.html', context)

def about(request):
    return render(request, 'msg_board/about.html', {'title': 'About'})
