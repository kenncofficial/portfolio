from django.urls import path
from .views import UserRegisterView, PasswordsChangeView, UserEditView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/',
     PasswordsChangeView.as_view(template_name='registration/change-password.html'),
      name='change-password'),

    #path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password-reset'),

    #path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password-reset-done'),

    #path('password_reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password-reset-confirm'),

    #path('password_success/', views.password_success, name='password_success'),
   
]
