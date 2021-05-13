from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField

# Create your models here.

class Home_Layout(models.Model):
    name = models.CharField(max_length=255)
    #header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    bio = RichTextField(blank=True, null=True)
    facebook_url = models.URLField(max_length=255, null=True, blank=True)
    instagram_url = models.URLField(max_length=255, null=True, blank=True)
    twitter_url = models.URLField(max_length=255, null=True, blank=True)
    github_url = models.URLField(max_length=255, null=True, blank=True)


    # def total_likes(self):
    # return self.likes.count()

    def __str__(self):
        return self.bio + '|' + str(self.name)

    def get_absolute_url(self):
        return reverse('home')

class About(models.Model):
	title = models.CharField(max_length=255)
	bio_1 = RichTextField(blank=True, null=True)
	birthday = models.CharField(max_length=255)
	website = models.URLField(max_length=255)
	phone = models.IntegerField()
	city = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	freelance= models.CharField(max_length=255)
	bio_2 = RichTextField(blank=True, null=True)

class Technology(models.Model):
	software = models.CharField(max_length=255)

class Intrest(models.Model):
	name_of_intrests = models.CharField(max_length=255)

class Resume(models.Model):
	title_tag = models.CharField(max_length=255)
	title = models.CharField(max_length=255) 
	year = models.CharField(max_length=255)
	content = RichTextField(blank=False)

class Experience(models.Model):
	title_tag = models.CharField(max_length=255)
	title = models.CharField(max_length=255) 
	year = models.CharField(max_length=255)
	content = RichTextField(blank=False)

class Service(models.Model):
	title = models.CharField(max_length=255)
	content = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Portfolio_Post(models.Model):
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	client = models.CharField(max_length=255)
	project_date = models.DateField(auto_now_add=True)
	Discription = RichTextField(blank=True, null=True)
	image = CloudinaryField('image', null=True, blank=True)
	project_url = models.URLField(max_length=255, default='non given')

	def self(self):
		return self.name + '|' + self.client