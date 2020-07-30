from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views
from .forms import *
from django.views import View
from .models import UserAdd
from django.core.mail import send_mail
from django.conf import settings
from random import randint

# Create your views here.
otp = ""
def index(request):
    if request.session.get("islogin"):
        return render(request,"afterlogin.html")
    return render(request,"nav.html")
    #it will go to the path you have defined in settings.py file and will find the page and return it
    #return HttpResponse("User app")

def home(request):
    return HttpResponse("Welcome to my user app home")

def myhome(request):
    return render(request,"faltu.html")

def login(request):
    if request.session.get("islogin"):
        return render(request,"afterlogin.html")
    else:
        form = Login()
        return render(request,"login.html",{'form':form})

def afterlogin(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid(): #validation
            email = form.cleaned_data['email']
            try:
                obj = UserAdd.objects.get(email=email)
            except Exception as e:
                error = "Invalid Email!!!!"
                form = Login()
                return render(request,"login.html",{"error":error,"form":form})
            else:
                passwd = form.cleaned_data['password']
                if obj.password == passwd:
                    request.session['email'] = email
                    request.session['islogin'] = "true"
                    return render(request,"afterlogin.html")
                else:
                    error = "Invalid password!!!"
                    form = Login()
                    return render(request,"login.html",{"error":error,"form":form})
            #return HttpResponse(f"{email}:{passwd}")
        else:
            error = "Invalid Form"
            form = Login()
            return render(request,"login.html",{'form':form,"error":error})
    else:
        return redirect("/user/login")
    
def signup(request):
    form = Signup()
    return render(request,"signup.html",{'form':form})

class aftersignup(View):
    # in View class the methods are the http methods
    def get(self,request):  #here get method is working for http get method request
        form = Signup()
        return render(request,"signup.html",{"form":form})
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            p1 = form.cleaned_data['password']
            p2 = form.cleaned_data['confirm_pass']
            if p1 == p2:
                try:
                    obj = UserAdd.objects.get(email=form.cleaned_data['email'])
                    #(email="simrangrover5@gmail.com")
                except Exception as e:
                    data = {
                        "email" : form.cleaned_data['email'],
                        "password" : p1,
                        "fname" : form.cleaned_data['fname'],
                        "lname" : form.cleaned_data["lname"],
                        "gender" : form.cleaned_data["gender"],
                        "pic"  : form.cleaned_data["pic"]               
                        }
                    UserAdd.objects.create(**data)
                    return redirect("/user/login/")
                else:
                    error = "Email already exist"
                    form = Signup()
                    return render(request,"signup.html",{"form":form,"error":error})
            else:
                error = "Password does not match!!! Try Agaia"
                form = Signup()
                return render(request,"signup.html",{"form":form,"error":error})
        else:
            error = "Invalid Form"
            form = Signup()
            return render(request,"signup.html",{"form":form,"error":error})

def logout(request):
    del request.session['email']
    del request.session['islogin']
    return redirect("/user/")

def forgot(request):
    form = Email_Form(request.POST)
    if form.is_valid():
        from_ = "simrangrover5@gmail.com"
        to_ = form.cleaned_data['email']
        try:
            obj = UserAdd.objects.get(email=to_)
        except:
            error = "Email is not registered"
            form = Login()
            return render(request,"login.html",{'form':form,"error":error})
        else:
            global otp
            subject = "OTP to reset your password"
            otp = randint(1000,9999)
            message = f"Enter this otp to change your password {otp}"
            send_mail(subject,message,from_,[to_,],auth_password=settings.EMAIL_HOST_PASSWORD)
            form = Otp()
            return render(request,"getotp.html",{"form":form})
    else:
        error = "Invalid form"
        form = Login()
        return render(request,"login.html",{'form':form,"error":error})

def getform(request):
    form = Email_Form()
    return render(request,"otpform.html",{"form":form})

def afterotp(request):
    form = Otp(request.POST)
    if form.is_valid():
        otp1 = form.cleaned_data['otp']
        if otp1 == str(otp):
            form = changepassword()
            return render(request,"getpass.html",{"form":form})
        else:
            error = "Incorrect otp"
            form = Login()
            return render(request,"login.html",{"form":form,"error":error})
    else:
        error = "Invalid form"
        form = Login()
        return render(request,"login.html",{"form":form,"error":error})

