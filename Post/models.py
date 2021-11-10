from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class  Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Post (models.Model):
    title = models.CharField(max_length=200)
    host= models.ForeignKey(User, models.CASCADE)
    category = models.ForeignKey(Category, models.SET_NULL, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.body[0:50]