from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(null=True)
    category = models.TextField(default="personal")
    deadline = models.DateTimeField(null=True)
    d_day = models.TextField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.TextField(default="Unknown")
    content = models.TextField()

    def __str__(self):
        return self.content