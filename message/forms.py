from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('to', 'body')
        labels = {
            "to": "Электронная почта",
            "body": "Сообщение"
        }
