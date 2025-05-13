"""
URL configuration for list_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import RegisterList, MakeRegisterView, LoginPageView, MakeLoginView
from dashboard.views import DashboardView, AddTasksView, DeletedTaskView,DoneTaskView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-page/', RegisterList.as_view(), name="register-url"),
    path('make-register/', MakeRegisterView.as_view(), name="make-register-url"),
    path('dashboard-page/', DashboardView.as_view(), name="dashboard-url"),
    path('add-task/', AddTasksView.as_view(), name="add-task-url" ),
    path('deleted-task/<int:pk>/', DeletedTaskView.as_view(), name="deleted-task-url"),
    path('done-task/<int:pk>/', DoneTaskView.as_view(), name="done-task-url"),
    path('login-page/', LoginPageView.as_view(), name="login-url"),
    path('make-login/', MakeLoginView.as_view(), name="make-login-url")
]
