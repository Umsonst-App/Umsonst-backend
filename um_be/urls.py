"""um_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/devices/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    path('api/', include('item.urls', namespace="item")),
    path('api/user/', include('user.urls',namespace="user"),),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/chat/', include('chat.urls', namespace="chat"),),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
