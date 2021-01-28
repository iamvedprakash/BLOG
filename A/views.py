from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def home(request):
    return HttpResponse('This is subapp!!!!!!!')

def list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'list.html', {'articles':articles})

def article_details(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug = slug)
    return render(request, 'datail.html', {'article':article})

@login_required(login_url="/acc/login/")
def create_article(request):
    if request.method == 'POST':
        form = forms.Create_Article(request.POST, request.FILES)
        if form.is_valid():
            # savve article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("article:list")
    else:
        form = forms.Create_Article()
    return render(request, 'create.html', {'form':form})
