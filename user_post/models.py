from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    '''
    here i create post model class for creating a blog
    '''

    title = models.CharField(max_length=50, unique=True)
    text = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete= models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title