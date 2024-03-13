from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=256)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class TaskType(models.Model):
    name = models.CharField(max_length=256)


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    deadline = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=255,
        choices=[
            ("Urgent", "Urgent"),
            ("High", "High"),
            ("Medium", "Medium"),
            ("Low", "Low"),
        ],
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.OneToOneField(Worker.objects.all(), on_delete=models.CASCADE)
