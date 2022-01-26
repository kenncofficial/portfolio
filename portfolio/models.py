from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Portfolio_Post(models.Model):
	name = models.CharField(max_length=255)
	client = models.CharField(max_length=255)
	project_date = models.DateField(auto_now_add=True)
	tools_used = models.CharField(max_length=255, null=True)
	Discription = RichTextField(blank=True, null=True)
	image = CloudinaryField('image', null=True, blank=True)
	image2 = CloudinaryField('image', null=True, blank=True)
	image3 = CloudinaryField('image', null=True, blank=True)
	project_url = models.URLField(max_length=255, default='non given')

	def self(self):
		return self.name + '|' + self.client