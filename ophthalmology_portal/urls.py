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

from django.conf import settings
from django.conf.urls.static import static
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
        "upload-exam-information/<int:exam_id>/",
        views.TestInformationCreationView.as_view(),
        name="exam_data_submission",
    ),
    path("patient-list/", views.PatientListView.as_view(), name="patient_list"),
    path(
        "patient-list/<int:patient>/",
        view=views.PatientInformationOtherView.as_view(),
        name="patient_history_information",
    ),
    path(
        "patient-list/<int:patient>/history/",
        view=views.PatientExamHistoryView.as_view(),
        name="patient_history_exam",
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
    path(
        "daily-exams/<int:patient>/",
        view=views.PatientInformationOtherView.as_view(),
        name="daily_patient",
    ),
    path(
        "daily-exams/exam/<int:exam_id>/",
        view=views.ExamDetailsView.as_view(),
        name="daily_exam_instance",
    ),
    path(
        "exam-request/",
        view=views.PatientExamCreationView.as_view(),
        name="exam_request",
    ),
    path(
        "personal-information/",
        view=views.PatientInformationView.as_view(),
        name="patient_information",
    ),
    path(
        "exam-confirmations/",
        view=views.ExamConfirmationsView.as_view(),
        name="exam_confirmations",
    ),
    path(
        "exam-confirmations/<int:id>/",
        view=views.ExamConfirmationView.as_view(),
        name="exam_confirmations",
    ),
    path("logout/", view=views.LogOutView.as_view(), name="log_out"),
    path(
        "prescription-history/",
        view=views.PrescriptionListView.as_view(),
        name="prescription_history",
    ),
    path(
        "prescription_pdf/<int:exam_id>",
        views.PrescriptionPDF.as_view(),
        name="prescription_download",
    ),
    path(
        "prescription_print/<int:exam_id>/",
        views.PrescriptionPrintPDF.as_view(),
        name="prescription_printer",
    ),
    path("claim_pdf/<int:exam_id>/", views.ClaimPDF.as_view(), name="claim_pdf"),
    path(
        "api/remove_exam/<int:exam_id>/<str:return_page>/",
        views.CancelExam.as_view(),
        name="cancel_exam",
    ),
    path(
        "api/progress-exam/<int:exam_id>",
        views.ProgressExam.as_view(),
        name="progress_exam",
    ),
    path(
        "api/regress-exam/<int:exam_id>",
        views.RegressExam.as_view(),
        name="regress_exam",
    ),
    path(
        "reschedule-exam/<int:exam_id>",
        views.RescheduleExam.as_view(),
        name="reschedule_exam",
    ),
    path(
        "insurance-claim/<int:exam_id>",
        views.InsuranceClaimView.as_view(),
        name="insurance_claim",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
