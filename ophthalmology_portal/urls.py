"""
URL configuration for ophthalmology_portal project.

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

from ophthalmology_portal.Core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePageView.as_view(), name="home_page"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path(
        "registration/information/",
        views.PatientInformationRegistrationView.as_view(),
        name="patient_registration",
    ),
    path("login/", views.LogInView.as_view(), name="log_in"),
    path("create-exam/", views.ExamCreationView.as_view(), name="create_exam"),
    path(
        "create-prescription/",
        views.PrescriptionCreationView.as_view(),
        name="create_prescription",
    ),
    path(
        "create-test-information/",
        views.TestInformationCreationView.as_view(),
        name="create_test_information",
    ),
    path("patient-list/", views.PatientListView.as_view(), name="patient_list"),
    path(
        "patient-list/<int:patient>/",
        view=views.PatientExamHistoryView.as_view(),
        name="patient_history",
    ),
    path(
        "exam-history/<int:exam_id>",
        view=views.ExamDetailsView.as_view(),
        name="exam_details",
    ),
    path(
        "exam-history/",
        view=views.PatientExamHistoryView.as_view(),
        name="personal_exam_history",
    ),
    path("daily-exams/", view=views.DailyExamsView.as_view(), name="daily_exams"),
    path("exam-request/", view=views.PatientExamCreationView.as_view(), name="exam_request"),
    path("personal-information/", view=views.PatientInformationView.as_view(), name="patient_information"),
    path("exam-confirmations/", view=views.ExamConfirmationsView.as_view(http_method_names=['get']), name="exam_confirmations"),
    path("exam-confirmations/<int:id>/", view=views.ExamConfirmationView.as_view(http_method_names=['post']), name="exam_confirmations"),
]
