from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

# CRUD - CREATE
def new(request):
    if request.method == "POST":
        print(request.POST)
        new_post = Post.objects.create(
            title = request.POST['title'],
            description = request.POST['description']
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')


# CRUD - READ
def detail(request, post_pk):
    # pk를 이용해서 전체 pk모델에서 특정 pk인 모델을 가지고 온다
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post' : post})


# CRUD - DELETE
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')
    # 이 함수의 역할은, 특정 pk의 post를 삭제해주는 것. 그런데 그 pk값은 어디서 가져오지?


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            description = request.POST['description']
        )
        return redirect('detail', post_pk)
    return render(request, 'edit.html', {'post' : post})
    