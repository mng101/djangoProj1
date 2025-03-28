"""
URL configuration for djangoProj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add URLS from the test1 application and authentication system
from django.urls import include

urlpatterns += [
    path('test1/', include('app1.urls')),
]

# Add URL maps to redirect the base URL to our test1 application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/app1/', permanent=True)),
]

