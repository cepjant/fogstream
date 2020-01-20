from django.contrib import admin
from django.template.response import TemplateResponse

from .models import Message


class MyAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        app_list = self.get_app_list(request)
        messages_count = Message.objects.count()
        messages_unsent = Message.objects.filter(status='NOT_SENT').count()
        context = {
            **self.each_context(request),
            'title': self.index_title,
            'app_list': app_list,
            'messages_c': messages_count,
            'messages_u': messages_unsent,
            **(extra_context or {}),
        }

        request.current_app = self.name

        return TemplateResponse(
            request, self.index_template or 'admin/index.html', context)
