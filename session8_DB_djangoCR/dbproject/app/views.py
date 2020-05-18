from django.shortcuts import render, redirect
from .models import Article
import datetime

# Create your views here.

def movie_defined_in_view(request):
    cnt_all = Article.objects.count()
    cnt_movie = Article.objects.filter(category = '영화').count()
    cnt_drama = Article.objects.filter(category = '드라마').count()
    cnt_entertain = Article.objects.filter(category = '예능').count()
    movie_articles = Article.objects.filter(category='영화')
    return render(request,'movie.html', {'movie_articles' : movie_articles, 'cnt_all': cnt_all,'cnt_movie' : cnt_movie, 'cnt_drama' : cnt_drama, 'cnt_entertain' : cnt_entertain})


def drama_defined_in_view(request):
    cnt_all = Article.objects.count()
    cnt_movie = Article.objects.filter(category = '영화').count()
    cnt_drama = Article.objects.filter(category = '드라마').count()
    cnt_entertain = Article.objects.filter(category = '예능').count()
    drama_articles = Article.objects.filter(category='드라마')
    return render(request,'drama.html', {'drama_articles' : drama_articles, 'cnt_all': cnt_all,'cnt_movie' : cnt_movie, 'cnt_drama' : cnt_drama, 'cnt_entertain' : cnt_entertain})


def entertain_defined_in_view(request):
    cnt_all = Article.objects.count()
    cnt_movie = Article.objects.filter(category = '영화').count()
    cnt_drama = Article.objects.filter(category = '드라마').count()
    cnt_entertain = Article.objects.filter(category = '예능').count()
    entertain_articles = Article.objects.filter(category='예능')
    return render(request,'entertain.html', {'entertain_articles' : entertain_articles, 'cnt_all': cnt_all,'cnt_movie' : cnt_movie, 'cnt_drama' : cnt_drama, 'cnt_entertain' : cnt_entertain})


def index_defined_in_view(request):
    cnt_all = Article.objects.count()
    cnt_movie = Article.objects.filter(category = '영화').count()
    cnt_drama = Article.objects.filter(category = '드라마').count()
    cnt_entertain = Article.objects.filter(category = '예능').count()
    all_articles = Article.objects.all()
    return render(request, 'index_in_templates.html', {'cnt_all': cnt_all,'cnt_movie' : cnt_movie, 'cnt_drama' : cnt_drama, 'cnt_entertain' : cnt_entertain, 'all_articles' :  all_articles })


def detail_defined_in_view(request, primary_key_of_the_article_that_i_clicked):
    cnt_all = Article.objects.count()
    cnt_movie = Article.objects.filter(category = '영화').count()
    cnt_drama = Article.objects.filter(category = '드라마').count()
    cnt_entertain = Article.objects.filter(category = '예능').count()
    article = Article.objects.get(pk=primary_key_of_the_article_that_i_clicked)
    return render(request, 'detail_in_templates.html', {'an_article_i_will_use_in_html' : article, 'cnt_all': cnt_all,'cnt_movie' : cnt_movie, 'cnt_drama' : cnt_drama, 'cnt_entertain' : cnt_entertain})


def new_defined_in_view(request):
    cnt_all = Article.objects.count()
    cnt_movie = Article.objects.filter(category = '영화').count()
    cnt_drama = Article.objects.filter(category = '드라마').count()
    cnt_entertain = Article.objects.filter(category = '예능').count()
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            date_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        )
        return redirect('detail_i_will_use_in_html', primary_key_of_the_article_that_i_clicked = new_article.pk)
    else:
        return render(request, 'new_in_templates.html', {'cnt_all': cnt_all,'cnt_movie' : cnt_movie, 'cnt_drama' : cnt_drama, 'cnt_entertain' : cnt_entertain})

