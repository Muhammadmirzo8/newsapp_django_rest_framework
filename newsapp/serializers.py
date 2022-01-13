from rest_framework.serializers import ModelSerializer, SlugField
from .models import Article, Topic

class ArticleSerializer(ModelSerializer):  
    topic = SlugField(read_only=True) 
    class Meta: 
        model = Article 
        fields = "__all__" 

class TopicSerializer(ModelSerializer): 
    class Meta: 
        model = Topic
        fields = "__all__" 