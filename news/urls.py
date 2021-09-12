from django.urls import path

from .views import *

urlpatterns=[
    path("",home,name="home"),
    path("second",second,name="second"),
    path("third",third,name="third"),
    path("fourth",fourth,name="fourth")
]