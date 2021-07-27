from django.urls import path
from project.apps.user import views
# from django.contrib.auth import views as auth_views
# from project.apps.user.forms import CustomSetPasswordForm

urlpatterns = [
    path('customer/email-register', views.CustomerEmailRegisterAPIView.as_view(), name='email_register'),
]    