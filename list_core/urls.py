from tkinter.font import names
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users.views import RegisterList, MakeRegisterView, LoginPageView, MakeLoginView, MakeLogoutView
from dashboard.views import DashboardView, AddTasksView, DeletedTaskView, DoneTaskView, UploadAvatarPicture


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-page/', RegisterList.as_view(), name="register-url"), # эндпоинт для страницы регистрации
    path('make-register/', MakeRegisterView.as_view(), name="make-register-url"),

    path('', DashboardView.as_view(), name="dashboard-url"), # эндпоинт для главной страницы, где задачи
    path('add-task/', AddTasksView.as_view(), name="add-task-url" ), # эндпоинт для, добавление задачи
    path('deleted-task/<int:pk>/', DeletedTaskView.as_view(), name="deleted-task-url"), # эндпоинт для, удаление задачи
    path('done-task/<int:pk>/', DoneTaskView.as_view(), name="done-task-url"), # эндпоинт для, того что бы отметить задание сделанным

    path('login-page/', LoginPageView.as_view(), name="login-url"), # эндпоинт для страницы логина
    path('make-login/', MakeLoginView.as_view(), name="make-login-url"),

    path('make-logout/', MakeLogoutView.as_view(), name="logout") # эндпоинт для выхода их аккаунта
]
