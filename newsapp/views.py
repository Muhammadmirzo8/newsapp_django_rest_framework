from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from  rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import ArticleSerializer,  TopicSerializer 
from .models import Article, Topic

class TopicListView(generics.ListAPIView): 
    queryset = Topic.objects.all() 
    serializer_class = TopicSerializer  
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["topic", ]
    ordering_fields = ["id", ]   

class TopicDetailView(generics.RetrieveAPIView): 
    queryset = Topic.objects.all() 
    serializer_class = TopicSerializer   

class ArticleDetailView(generics.RetrieveAPIView): 
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer 

class ArticleListView(generics.ListAPIView): 
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["name", "topic", ]
    ordering_fields = ["date", "topic", ] 
    permission_classes = (AllowAny, ) 


# admin of app 

class TopicListCreateView(generics.ListCreateAPIView): 
    queryset = Topic.objects.all() 
    serializer_class = TopicSerializer  
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["name", ]
    ordering_fields = ["name", ]  
    permission_classes = (IsAuthenticated, )

class TopicDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Topic.objects.all() 
    serializer_class = TopicSerializer   
    permission_classes = (IsAuthenticated, ) 

class ArticleListCreateView(generics.ListCreateAPIView): 
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["name", "topic", ]
    ordering_fields = ["date", "topic", ] 
    permission_classes = (IsAuthenticated, )   

class ArticleDetailUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer 
    permission_classes = (IsAuthenticated, )
