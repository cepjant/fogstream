from django.urls import path, include

from .views import *

urlpatterns = [
    path('', UserLogin.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('message/', include('message.urls'), name='message'),
]
