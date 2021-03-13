from django.contrib import admin
from .models import Home_Layout, Category, Portfolio_Post, About, Intrest, Resume, Experience, Service, Technology
# Register your models here.

admin.site.register(Home_Layout)
admin.site.register(About)
admin.site.register(Technology)
admin.site.register(Intrest)
admin.site.register(Resume)
admin.site.register(Experience)
admin.site.register(Service)
admin.site.register(Portfolio_Post)
admin.site.register(Category) 