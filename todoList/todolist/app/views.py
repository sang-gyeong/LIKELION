from django.shortcuts import render, redirect
from .models import Task, Comment
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required



def cal_d_day(deadline):
    str_now = datetime.strftime(datetime.now(), '%Y-%m-%d')
    compare_now = datetime.strptime(str_now, '%Y-%m-%d')
    if deadline is not None:
        compare_deadline = datetime.strptime(deadline, '%Y-%m-%d')
        d_day = (compare_now - compare_deadline).days
        if d_day == 0:
            return "-0"
        elif d_day > 0:
            return "+" + str(d_day)
        elif d_day < 0:
            return str(d_day)
    return None


def home(request):
    all_tasks = Task.objects.all().order_by('deadline')
    todo_tasks = []
    for task in all_tasks:
        if is_done(task.deadline) is False:
            todo_tasks.append(task)
    return render(request, 'home.html', {'todo_tasks': todo_tasks})

@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_task = Task.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
            category=request.POST['category'],
            d_day=cal_d_day(request.POST['deadline']),
            author = request.user
        )
        return redirect('detail', new_task.pk)
    return render(request, 'new.html')


def detail(request, task_pk):
    task = Task.objects.get(pk=task_pk)

    if request.method == "POST":
        Comment.objects.create(
            task = task,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', task_pk)
    return render(request, 'detail.html', {'task': task})


def edit(request, task_pk):
    task = Task.objects.get(pk=task_pk)
    if request.method == 'POST':
        edited_task = Task.objects.filter(pk=task_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            deadline=request.POST['deadline'],
            category=request.POST['category'],
            d_day=cal_d_day(request.POST['deadline'])
        )
        return redirect('detail', task_pk)
    return render(request, 'edit.html', {'task': task})


def delete(request, task_pk):
    task = Task.objects.get(pk=task_pk)
    task.delete()
    return redirect('home')

def delete_comment(request, task_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', task_pk)


def personal(request):
    all_personal_tasks = Task.objects.filter(
        category="personal").order_by('deadline')
    personal_tasks = []
    for task in all_personal_tasks:
        if is_done(task.deadline) is False:
            personal_tasks.append(task)
    return render(request, 'personal.html', {'personal_tasks': personal_tasks})


def work(request):
    all_work_tasks = Task.objects.filter(category="work").order_by('deadline')
    work_tasks = []
    for task in all_work_tasks:
        if is_done(task.deadline) is False:
            work_tasks.append(task)
    return render(request, 'work.html', {'work_tasks': work_tasks})


def likelion(request):
    all_likelion_tasks = Task.objects.filter(
        category="likelion").order_by('deadline')
    likelion_tasks = []
    for task in all_likelion_tasks:
        if is_done(task.deadline) is False:
            likelion_tasks.append(task)
    return render(request, 'likelion.html', {'likelion_tasks': likelion_tasks})


def done(request):
    tasks = Task.objects.all().order_by('-deadline')
    done_tasks = []
    for task in tasks:
        if is_done(task.deadline) is True:
            done_tasks.append(task)
    return render(request, 'done.html', {'done_tasks': done_tasks})


def is_done(deadline):
    now = datetime.strftime(datetime.now(), '%Y-%m-%d')
    if deadline is not None:
        date_to_compare = datetime.strftime(
            deadline + timedelta(hours=23, minutes=59), '%Y-%m-%d')
        if date_to_compare < now:
            return True
    return False


def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user)>0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', {'error' : error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('home')
    return render(request, 'registration/signup.html')



def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (found_user is None):
            error = "아이디 또는 비밀번호가 틀렸습니다"
            return render(request, 'registration/login.html', {'error' : error})

        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next', '/'))
    
    return render(request, 'registration/login.html')



def logout(request):
    auth.logout(request)
    return redirect('home')