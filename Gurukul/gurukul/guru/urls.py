from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home ),
    path('get/',views.get_bot_response),
]