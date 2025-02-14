from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.patient_registration, name='patient_registration'),
    path('success/', views.patient_success, name='patient_success'),
]
