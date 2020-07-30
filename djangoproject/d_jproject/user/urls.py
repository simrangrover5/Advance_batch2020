from django.urls import path
from . import views

urlpatterns = [
    path("",views.index), #"" --> localhost/user, domain/user
    path("home/",views.home), # localhost/user/home --> home function
    path("index/",views.myhome), #localhost/user/index --> myhome
    path("login/",views.login),
    path("afterlogin/",views.afterlogin),
    path("signup/",views.signup),
    path("aftersignup/",views.aftersignup.as_view()),
    path("logout/",views.logout),
    path("forgot/",views.getform),
    path("getotp/",views.forgot),
    path("afterotp/",views.afterotp)
]
#till aftersignup the view was our function now we have to change
#we want our view to be a class