from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import LoginForm, UserRegistrationForm


class UserRegister(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        django_logout(request)
        return render(request, 'login/register.html',
                      context={'user_form': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            result = render(request, 'login/register_done.html',
                            context={'new_user': new_user})
        else:
            result = HttpResponse('Invalid login.')
        return result


class UserLogin(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = LoginForm()
            result = render(request, 'login/login.html', context={'form': form})
        else:
            result = redirect('send_message')
        return result

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    result = redirect('send_message')
                else:
                    result = HttpResponse('Disabled account')
            else:
                result = HttpResponse('Invalid login')
        return result


def logout(request):
    django_logout(request)
    return redirect('login')
