from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from users.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

class RegisterList(TemplateView):
    """ Вью для показа страницы регистрации """
    template_name = 'register.html'


class MakeRegisterView(View):
    """ Вью для регистрации пользователя  """

    def post(self, request, *args, **kwargs):
        data = request.POST
        password1 = data.get('password1')
        password2 = data.get('password2')
        email = data.get('email')

        if password1 != password2:
            messages.error(request, "Пароли не совпадают")
            return redirect('register-url')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Пользователь с таким email уже существует.")
            return redirect('register-url')

        user = CustomUser.objects.create_user(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=email,
            password=password1
        )
        login(request, user)

        send_email(email)

        return redirect("dashboard-url")



class LoginPageView(TemplateView):
    """ Вью для страницы логина  """
    template_name = "login.html"


class MakeLoginView(View):
    """ Вью для того что бы зарегистрировать пользователя  """

    def post(self, request, *args, **kwargs):
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.error(request, "пользователь не найден.")
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            return redirect('dashboard-url')

        messages.error(request, "Неверный пароль.")
        return redirect('login-url')


class MakeLogoutView(View):
    """Вью для выхода из аккаунта"""
    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'login.html', {})



def send_email(to_email):
    """Отправка письма после регистрации"""
    subject = 'Добро пожаловать'
    message = 'Вы успешно зарегистрировались на нашем сайте. Теперь задачи под моим контролем и все они не выполнятся наверное'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [to_email]

    send_mail(subject, message, from_email, recipient_list)