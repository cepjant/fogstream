import json
import requests

from smtplib import SMTPAuthenticationError

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from project import settings
from project.celery import app
from .forms import MessageForm
from .models import Message



@app.task
def async_send_mail(body, to):
    """
    Асинхронно через celery отправялет email
    :return: None
    """
    message = Message(to=to, body=body)
    try:
        send_mail('...', body, settings.EMAIL_HOST_USER, [to])
        message.status = 'SENT'
        message.save()
    except SMTPAuthenticationError:
        message.status = 'NOT_SENT'
        message.save()


class SendMessage(LoginRequiredMixin, View):
    def get(self, request):
        form = MessageForm()
        return render(request, 'message/sending.html', context={'form': form})

    def post(self, request):
        form = MessageForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            body, to = cd['body'], cd['to']
            #r = requests.get('http://jsonplaceholder.typicode.com/users')
            # Сайт, используяемый для парсинга, недоступен без VPN.
            #senders = json.loads(r.text)
            #to = {}
            #for s in senders:
            #    if s['email'].lower() == cd['sender'].lower():
            #        to = s
            #if not sender:
            #    async_send_mail.delay(body, to)
            #else:
            #
            #MESSAGE = """
            #От {}
            #{}
            #Город {}
            #улица {}
            #квартира {}
            #почтовый индекс {}
            #Email {}
            #Номер телефона {}
            #"""
            #    body = MESSAGE.format(
            #sender['name'], body, sender['address']['city'],
            #sender['address']['street'], sender['address']['suite'],
            #sender['address']['zipcode'], email, sender['phone']
            #)
            async_send_mail.delay(body, to)

        return render(request, 'message/index.html')
