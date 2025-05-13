from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from users.models import CustomUser


class RegisterList(TemplateView):
    """ вью для показа страницы регистрации """
    template_name = 'register.html'


class MakeRegisterView(View):
    """ вьюшка для регистрации пользователя  """

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
            messages.error(request, "пользователь не найден.")
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            return redirect('dashboard-url')

        messages.error(request, "Неверный пароль.")
        return redirect('login-url')


class MakeLogoutView(View):
    """Вьюшка для выхода из аккаунта"""
    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'login.html', {})

