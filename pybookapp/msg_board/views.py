from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.generic import TemplateView
from msg_board.models import Users

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['user_name', 'email', 'user_message']

def user_list(request, template_name='msg_board/user_list.html'):
    user = Users.objects.all()
    data = {}
    data['object_list'] = user
    return render(request, template_name, data)
