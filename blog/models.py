from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField
from portfolio.models import Category
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=100, null=True)
    
    def __str__(self):
        return self.name

# Create your models here.
class BlogPost(models.Model):
    image = CloudinaryField('image', null=True, blank=True)
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255, default='snippet test')
    slug = models.SlugField(unique=True, max_length=100, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content1 = RichTextField(blank=True, null=True)
    blog_quote = models.CharField(max_length=500, blank=True)
    content2 = RichTextField(blank=True, null=True)
    tags = TaggableManager()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('BlogPost-details', kwargs={'slug': self.slug})

class BlogComment(models.Model):
    blogpost_connected =  models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ' , ' + self.blogpost_connected.title[:40]

    def get_absolute_url(self):
        return reverse('update_comment', kwargs={'pk': self.pk})
