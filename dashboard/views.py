from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from dashboard.models import Task
from users.models import CustomUser


# Create your views here.
class DashboardView(TemplateView):
    """ вьюшка для туду листа """
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = {
            'user':user,
            'task': Task.objects.filter(is_done=False, user=user),
            'done_task': Task.objects.filter(is_done=True, user=user)

        }
        return context



class AddTasksView(View):
    """ вьюшка для добавления новых задач """
    def post(self, request):
        data = request.POST
        task = data['tasks']

        task = Task.objects.create(user=request.user,  text=task)
        task.save()
        return redirect('dashboard-url')


class DeletedTaskView(View):
    """ вьюшка для того что бы удалить задачи """
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk, user = request.user)
        task.delete()

        return redirect('dashboard-url')

class DoneTaskView(View):
    """ вьюшка для того что бы пометить задачи помеченными """
    def post(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'] , user=request.user)
        task.is_done = True
        task.save()

        return redirect("dashboard-url")

