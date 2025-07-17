from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list_view, name='home'),
    path('news/<int:pk>/', views.news_detail_view, name='news_detail'),
    path('news/add/', views.add_news_view, name='add_news'),
    path('news/<int:pk>/delete/', views.delete_news_view, name='delete_news'),
]
