from django.db import models
from users.models import CustomUser


# Create your models here.
class Task(models.Model):
    """Модель для задач"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)