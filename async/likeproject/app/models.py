from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    img_url = models.TextField()
    price = models.IntegerField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # like_users = models.ManyToManyField(Profile, related_name='like_posts')

    def __str__(self):
        return self.title

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     like_list = models.ManyToManyField(Post, related_name='like_list')
#     wish_list = models.ManyToManyField(Post, related_name='wish_list')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'likes')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='likes')

class Wish(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'wishes')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='wishes')
