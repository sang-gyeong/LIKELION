from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Wish
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts': posts })

@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

@login_required(login_url='/registration/login')
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    existing_like = Like.objects.filter(
        post = post,
        user = request.user
    )
    existing_wish = Wish.objects.filter(
        post = post,
        user = request.user
    )

    if existing_like.count() > 0 :
        is_like = True
    else :
        is_like = False

    if existing_wish.count() > 0 :
        is_wish = True
    else :
        is_wish = False


    if (request.method == 'POST'):
        Comment.objects.create(
            post = post, 
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', post_pk)

    return render(request, 'detail.html', {'post': post , 'is_like' : is_like , 'is_wish' : is_wish})

@login_required(login_url='/registration/login')
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
          title = request.POST['title'],
          content = request.POST['content']
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post}) 

@login_required(login_url='/registration/login')
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

@login_required(login_url='/registration/login')
def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', { 'error' : error })

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')

    return render(request, 'registration/signup.html')

def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', { 'error': error })

        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


@csrf_exempt
@login_required(login_url='/registration/login')
def like(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']
        
        existing_like = Like.objects.filter(
            post = Post.objects.get(pk=post_pk),
            user = request.user
        )

        #좋아요 취소
        if existing_like.count() > 0 :
            is_like = False
            existing_like.delete()
            
        #좋아요 생성
        else:
            is_like = True
            Like.objects.create(
                post = Post.objects.get(pk=post_pk),
                user = request.user
            )

        post_likes = Like.objects.filter(
            post = Post.objects.get(pk=post_pk)
        )

        response = {
            'like_count' : post_likes.count(),
            'is_like' : is_like
        }

        return HttpResponse(json.dumps(response))


@csrf_exempt
@login_required(login_url='/registration/login')
def wish(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']
        
        existing_wish = Wish.objects.filter(
            post = Post.objects.get(pk=post_pk),
            user = request.user
        )

        if existing_wish.count() > 0 :
            is_wish = False
            existing_wish.delete()
            
        else:
            is_wish = True
            Wish.objects.create(
                post = Post.objects.get(pk=post_pk),
                user = request.user
            )
        post_wishes = Wish.objects.filter(
            post = Post.objects.get(pk=post_pk)
        )

        response = {
            'wish_count' : post_wishes.count(),
            'is_wish' : is_wish
        }
        return HttpResponse(json.dumps(response))
    


@login_required(login_url='/registration/login')
def mypage(request):
    posts = Post.objects.all()
    like_posts = []
    wish_posts = []

    for post in posts :
        like = Like.objects.filter(
            post = post,
            user = request.user
        )
        wish = Wish.objects.filter(
            post = post,
            user = request.user
        )
        if like :
            like_posts.append(post)
        if wish :
            wish_posts.append(post)

    return render(request, 'mypage.html', {'like_posts' : like_posts , 'wish_posts' : wish_posts})