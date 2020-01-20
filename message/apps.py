from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MessageConfig(AppConfig):
    name = 'message'


class MyAdminConfig(AdminConfig):
    default_site = 'message.admin.MyAdminSite'
