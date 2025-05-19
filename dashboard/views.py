from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from dashboard.models import Task

class DashboardView(TemplateView):
    """ Вьюшка для туду-листа """
    template_name = "dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login-url')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = {
            'user': user,
            'task': Task.objects.filter(is_done=False, user=user),
            'done_task': Task.objects.filter(is_done=True, user=user)
        }
        return context


class AddTasksView(View):
    """ вьюшка для добавления новых задач """
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login-url')

        data = request.POST
        Task.objects.create(user=request.user, text=data.get('tasks'))
        return redirect('dashboard-url')


class DeletedTaskView(View):
    """ вьюшка для того что бы удалить задачи """
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login-url')

        task = get_object_or_404(Task, id=pk, user=request.user)
        task.delete()
        return redirect('dashboard-url')


class DoneTaskView(View):
    """ вьюшка для того что бы пометить задачи помеченными """
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('login-url')

        task = get_object_or_404(Task, id=pk, user=request.user)
        task.is_done = True
        task.save()
        return redirect("dashboard-url")

class UploadAvatarPicture(View):
    """ вьюшка для того что бы добавить фото профиля  """
    def post(self, request):

        image = request.FILES.get('image')
        if image:
            request.user.avatar_image = image
            request.user.save()
        return redirect("dashboard-url")