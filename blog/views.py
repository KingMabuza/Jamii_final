from django.shortcuts import render
from . import templates
from newsapi import NewsApiClient
from .models import Blog
from django.contrib import messages


# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key="922bccdaca334a0daa16d903ff1b8e26")
    all_articles = newsapi.get_everything(q='afcfta',
                                          language='en',
                                          sort_by='relevancy',
                                          page_size=3)

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    url = []
    author = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        author.append(myarticles['author'])
    mylist = zip(news, desc, img, url, author)

    obj = Blog.objects.get(id=1)
    blog_post = {
        'title': obj.title,
        'cover': obj.cover,
        'author': obj.author,
        'date': obj.date_posted,
        'content': obj.content,
        'subtitle': obj.subtitle
    }

    return render(request, 'blog/home.html', context={"mylist": mylist, 'post': blog_post})


def about(request):
    return render(request, 'blog/about.html')


def blog(request):
    return render(request, 'blog/blog.html')


def contact(request):
    return render(request, 'blog/contact.html')


def events(request):
    return render(request, 'blog/events.html')


def explorer(request):
    return render(request, 'blog/explorer.html')


def glossary(request):
    return render(request, 'blog/glossary.html')


def login(request):
    return render(request, 'blog/login.html')


def news(request):
    return render(request, 'blog/news.html')


def opportunities(request):
    return render(request, 'blog/opportunities.html')


def signup(request):
    return render(request, 'blog/signup.html')
