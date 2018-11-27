from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from msg_board.models import Member,Message
from pymongo import MongoClient
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from msg_board.forms import UserRegisterForm
import urllib.parse

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'msg_board/home.html', context=None)

class MemberListProperView(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching members via Djongo")
        members = Member.objects.all()
        print(members)
        data = {}
        data["name"] = "Travolta"
        data["email"] = "Travolta@gmail.com"
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

class MemberListProperView1(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching members using PyMongo")
        client = MongoClient(port=27017)
        db = client.pybook_test1
        result = db.msg_board_member.find()
        print(result)
        data = {}
        data['object_list'] = result
        return render(request, 'msg_board/player.html', {"data": data})


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
    fields = ['text', 'like_count']
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
    # update directly here
    success_url = reverse_lazy('msg_board:message_list')

class MessageViewDetail(DetailView):
    model = Message



# DB below ---------
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('msg_board-home')
    else:
        form = UserRegisterForm()
    return render(request, 'msg_board/registration/register.html', {'form': form})

def home(request):
    # context = {
    #     'messages': messages
    # }
    return render(request, 'msg_board/home.html')

def about(request):
    return render(request, 'msg_board/about.html', {'title': 'About'})
