from django.contrib import admin
from django.urls import path  
from information import views

urlpatterns = [
    path('', views.news_list_view, name='home'),
    path('news/<int:pk>/', views.news_detail_view, name='news_detail'),
    path('add/', views.add_news_view, name='add_news'),
]
