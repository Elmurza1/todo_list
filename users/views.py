from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


# Create your views here.
class RegisterList(TemplateView):
    """ вью для показа страницы регистрации """
    template_name = 'register.html'


class MakeRegisterView(View):
    """ вьюшка для регистрации пользователя  """
    def post(self, request, *args, **kwargs):
        data = request.POST
        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']

            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password1
            )
            user.save()
            login(request, user)


        print(data)
        return redirect("dashboard-url")

class LoginPageView(TemplateView):
    """ вьюшка для страницы логина  """
    template_name = "login.html"


class MakeLoginView(View):
    """ вьшка для того что бы зарегистрировать пользователя  """

    def post(self, request, *args, **kwargs):
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            print(user)
            return redirect('dashboard-url')
        else:
            return redirect('login-url')


