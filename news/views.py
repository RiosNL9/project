from django.shortcuts import render
from .models import News,Category,New

# Create your views here.

def index(request):
    category = Category.objects.all()
    new = New.objects.all()
    news = News.objects.all()
    return render(request,'index.html',{'data':news,'Category':category,'data1':new})





def category(request):
    new = New.objects.all()
    category = Category.objects.all()
    news = News.objects.all()
    return render(request,'category.html',{'data':news,'Category':category,'new':new})

def detail(req,id):
    data = News.objects.get(id=id)
    return render(req,'single.html',{'data':data})

def contact(request):
    return render(request,'contact.html')

def single(request):
    return render(request,'single.html')
