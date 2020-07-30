from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("addblog/",views.addblog),#/blog/
    path("blogadd/",views.blogadd),
    path("myblog/",views.myblog),
    path("allblog/",views.allblog),
    path("api/",views.Myapi.as_view()) #/blog/api --> api --> page
]