from django.urls import path
from .views import HomeView, PortfolioDetailView


urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('portfolio/<int:pk>', PortfolioDetailView.as_view(), name='portfolio-details'),

]
