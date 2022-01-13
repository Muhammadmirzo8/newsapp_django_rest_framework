from django.urls import path
from .views import TopicDetailView, TopicListView, ArticleListView, ArticleDetailView

urlpatterns = [ 
    path('', ArticleListView.as_view(), name='article-list'), 
    path('news/<int:pk>/', ArticleDetailView.as_view(), name='article-list'),
    path('topics/', TopicListView.as_view(), name='topic-list'), 
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),

]
