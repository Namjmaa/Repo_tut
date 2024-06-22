from django.utils import timezone
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    task_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Note(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
