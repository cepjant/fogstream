from django.db import models


class Message(models.Model):
    SENT = 'SENT'
    NOT_SENT = 'NOT_SENT'

    STATUS_CHOICES = (
        (SENT, 'Отправлено'),
        (NOT_SENT, 'Не отправлено')
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=NOT_SENT
    )
    to = models.EmailField(
        verbose_name='Кому'
    )
    body = models.TextField(
        verbose_name='Содержание'
    )
