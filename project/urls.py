"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from university.api.views import UniversityModelViewset
from rest_framework.routers import DefaultRouter
from django.views.generic.base import TemplateView
router = DefaultRouter()
router.register(r'universities', UniversityModelViewset, basename='universities')

urlpatterns = [
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new

    ]
