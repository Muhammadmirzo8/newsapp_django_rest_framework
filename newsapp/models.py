from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model): 
    name = models.CharField(max_length=100)  

    def __str__(self): 
        return self.name   


class Article(models.Model): 
    name = models.CharField(max_length=200) 
    text = models.TextField() 
    photo = models.FileField(upload_to="photo/", null=True, blank=True)
    video = models.FileField(upload_to="video/", null=True, blank=True) 
    date = models.DateTimeField(auto_now_add=True) 
    views = models.PositiveIntegerField(default=0) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self): 
        return self.name   

    class Meta: 
        ordering = ['topic', ]
