"""blogAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from newsapp.views import  TopicListCreateView, ArticleListCreateView, ArticleDetailUpdateDestroyView, TopicDetailUpdateDestroyView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('newsapp.urls')),

    path('r^get^token/', TokenObtainPairView.as_view()), 
    path('r^refresh^token/', TokenRefreshView.as_view()), 

    path('r^admin^/', TopicListCreateView.as_view(), name='topic-list-create'),   
    path('r^admin^topic/<int:pk>/',TopicDetailUpdateDestroyView.as_view(), name='topic-settings'), 
    path('r^admin^news/', ArticleListCreateView.as_view(), name='news-list-create'),  
    path('r^admin^news/<int:pk>/',ArticleDetailUpdateDestroyView.as_view(), name='article-settings'),
]
