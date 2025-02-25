from django.urls import path

from .views import appointment_request_page, appointment_success

urlpatterns = [
    path("appointment-request/", appointment_request_page, name="appointment_request"),
    path(
        "appointment-success/", appointment_success, name="appointment_success"
    ),  # ADD THIS
]
