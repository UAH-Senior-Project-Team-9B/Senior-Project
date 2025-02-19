"""
URL configuration for ophthamology_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from ophthamology_portal.Core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePageView.as_view(), name="home_page"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path(
        "registration/<int:token>/",
        views.RegistrationView.as_view(),
        name="registration",
    ),
    path(
        "registration/information/",
        views.RegistrationInformationView.as_view(),
        name="registration-information",
    ),
    path("login/", views.LogInView.as_view(), name="log_in"),
    path("token/", views.TokenGenerationView.as_view(), name="token_gen"),
]
