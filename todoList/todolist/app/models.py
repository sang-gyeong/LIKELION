from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(null=True)
    category = models.TextField(default="personal")
    deadline = models.DateTimeField(null=True)
    d_day = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content

class Post(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    description = models.CharField(max_length=50)
    img = models.TextField()

    def __str__(self):
        return self.description