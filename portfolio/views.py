from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Home_Layout, About, Intrest, Resume, Experience, Service
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeView(ListView):
    context_object_name = 'home'
    template_name = 'index.html'
    queryset = Home_Layout.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["Abouts"] = About.objects.all()
        context["Intrests"] = Intrest.objects.all()
        context["Resumes"] = Resume.objects.all()
        context["Services"] = Service.objects.all()
        context["Experiences"] = Experience.objects.all()
        context["Home_Layouts"] = self.queryset
        return context