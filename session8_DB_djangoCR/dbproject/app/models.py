from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content= models.TextField()
    category = models.CharField(max_length=20, default="영화")
    date_time = models.CharField(max_length=200)


    def __str__(self):
        return self.title
