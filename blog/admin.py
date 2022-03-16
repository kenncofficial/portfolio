from django.contrib import admin
from .models import BlogPost, Category, BlogComment
# Register your models here.

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(BlogComment)