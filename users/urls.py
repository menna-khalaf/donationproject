from django.urls import path
from .views import UserRegisterView, UserProfileEditView , ActivateAccountView , email_login_view
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

app_name = 'users'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/done/', TemplateView.as_view(template_name='users/register_done.html'), name='register_done'),
    path('profile/edit/', UserProfileEditView.as_view(), name='profile-edit'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    path('login/', email_login_view, name='login'),

]
