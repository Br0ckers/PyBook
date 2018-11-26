from django import forms
from msg_board.models import Message, Member



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'date', 'like_count']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'password']
