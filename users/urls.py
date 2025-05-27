from django.urls import path
from .views import UserRegisterView, UserProfileEditView
from django.views.generic import TemplateView

app_name = 'users'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/done/', TemplateView.as_view(template_name='users/register_done.html'), name='register_done'),
    path('profile/edit/', UserProfileEditView.as_view(), name='profile-edit'),
]
