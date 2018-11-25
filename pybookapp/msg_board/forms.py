from django import forms


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'date', 'like_count']

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['user_name', 'email', 'password']
