from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from msg_board.models import Player,Message
from pymongo import MongoClient
import urllib.parse

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

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
        result = db.msg_board_player.find()
        print(result)
        data = {}
        data['object_list'] = result
        return render(request, 'player.html', {"data": data})

#new stuff

class UserList(ListView):
    model = Player

class UserCreate(CreateView):
    model = Player
    fields = ['user_name', 'email', 'password']
    success_url = reverse_lazy('msg_board:user_list')

class UserUpdate(UpdateView):
    model = Player
    fields = ['user_name', 'email', 'password']
    success_url = reverse_lazy('msg_board:user_list')

class UserDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('msg_board:user_list')

class UserViewDetail(DetailView):
    model = Player

class UserRemindPassword(UpdateView):
    model = Player
    fields = ['user_name', 'email', 'password']
    success_url = reverse_lazy('msg_board:user_list')

# Message views

class MessageViewAll(ListView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = ['text']
    success_url = reverse_lazy('msg_board:message_list')

class MessageUpdate(UpdateView):
    model = Message
    fields = ['text', 'like_count']
    success_url = reverse_lazy('msg_board:message_list')

class MessageDelete(DeleteView):
    model = Message
    print("delete called")
    success_url = reverse_lazy('msg_board:message_list')

class MessageLike(UpdateView):
    model = Message
    #model.increment_like(self)
    fields = ['text']
    success_url = reverse_lazy('msg_board:message_list')

class MessageViewDetail(DetailView):
    model = Message
