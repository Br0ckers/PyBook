from django import forms


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'date', 'like_count']

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'password']
