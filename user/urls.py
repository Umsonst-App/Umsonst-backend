from django.urls import path, include
from .views import (
    UserCreate,
    SetPassword,
    UserViewMe,
    UserView,
)
import django_rest_passwordreset

app_name = 'user'

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password_reset/<str:token>/', SetPassword.as_view(), name='password_reset_change'),
    path('me/', UserViewMe.as_view(),name='my-user'),
    path('<slug:slug>/', UserView.as_view(), name='user' ),
    ]
