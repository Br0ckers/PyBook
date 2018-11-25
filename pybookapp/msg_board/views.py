from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from msg_board.models import Member,Message
from pymongo import MongoClient
import urllib.parse

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class MemberListProperView(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching members via Djongo")
        members = Member.objects.all()
        print(members)
        data = {}
        data['object_list'] = members
        return render(request, 'member_list.html', {"data": data})

class MemberListProperView1(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching members using PyMongo")
        client = MongoClient(port=27017)
        db = client.pybook_test1
        result = db.msg_board_member.find()
        print(result)
        data = {}
        data['object_list'] = result
        return render(request, 'member.html', {"data": data})

#new stuff

class MemberViewAll(ListView):
    model = Member
    success_url = reverse_lazy('msg_board:member_list')

class MemberCreate(CreateView):
    model = Member
    fields = ['name', 'email', 'password']
    success_url = reverse_lazy('msg_board:member_list')

class MemberUpdate(UpdateView):
    model = Member
    fields = ['name', 'email', 'password']
    success_url = reverse_lazy('msg_board:member_list')

class MemberDelete(DeleteView):
    model = Member
    success_url = reverse_lazy('msg_board:member_list')

class MemberViewDetail(DetailView):
    model = Member
    success_url = reverse_lazy('msg_board:member_list')

class MemberAddFriend(UpdateView):
    model = Member
    fields = ['friends']
    success_url = reverse_lazy('msg_board:member_list')

class MemberRemindPassword(UpdateView):
    model = Member
    fields = ['name', 'email', 'password']
    success_url = reverse_lazy('msg_board:member_list')

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
    success_url = reverse_lazy('msg_board:message_list')

class MessageLike(UpdateView):
    model = Message
    #model.increment_like(self)
    success_url = reverse_lazy('msg_board:message_list')

class MessageViewDetail(DetailView):
    model = Message
