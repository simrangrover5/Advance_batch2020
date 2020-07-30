from django.shortcuts import render
from django.http import HttpResponse
from .forms import Blog
from .models import Addblog
from user.models import UserAdd
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Addblogserializer
# Create your views here.
def index(request):
    return HttpResponse("<h1 style='color:red'>Welcome to blog app</h1> ")

def addblog(request):
    form = Blog()
    return render(request,"blogform.html",{"form":form})

def blogadd(request):
    form = Blog(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        post = form.cleaned_data['post']
        author = request.session['email']  #this is only the mail
        #while inserting the data into addblog you have to enter the object of useradd model
        Addblog.objects.create(title=title,post=post,author=UserAdd.objects.get(email=author))
        error = "Successfully uploaded the blog".upper()
        return render(request,"afterlogin.html",{"error":error})
    else:
        error = "Invalid Form"
        form = Blog()
        return render(request,"blogform.html",{"form":form,"error":error})

def myblog(request):
    user = request.session['email']
    obj = UserAdd.objects.get(email=user)
    id = obj.id #primary key
    blogs = Addblog.objects.filter(author=id)
    allblogs = []
    for i in blogs:
        d = {
            'title' : i.title,
            'post' : i.post,
            'date' : i.date,
            'author' : i.author
        }
        allblogs.append(d)
    return render(request,"showblog.html",{"blogs":allblogs})

def allblog(request):
    blogs = Addblog.objects.all()
    allblogs = []
    for i in blogs:
        d = {
            'title' : i.title,
            'post' : i.post,
            'date' : i.date,
            'author' : i.author
        }
        allblogs.append(d)
    return render(request,"showblog.html",{"blogs":allblogs})

class Myapi(APIView):
    def get(self,request):  #handle get method request
        all_blogs = Addblog.objects.all()
        blogs = Addblogserializer(all_blogs,many=True)
        return Response(blogs.data)
    def post(self,request):  #try by yourself, request.data
        pass

#djangorestframework -->templates (for different http method)
#1. pip install djangorestframework
#2. add the rest_framework in your apps 
#3. serializers.py --> data which you want to share through api and you will which model to have your data
