from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Portfolio_Post, Category
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeView(ListView):
    context_object_name = 'home'
    template_name = 'index.html'
    queryset = Category.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["Portfolio_Posts"] = Portfolio_Post.objects.all()
        return context

class PortfolioDetailView(DetailView):
    model = Portfolio_Post
    template_name = 'portfolio-details.html'