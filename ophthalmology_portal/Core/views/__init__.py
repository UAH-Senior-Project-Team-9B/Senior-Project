from ophthalmology_portal.Core.views.appointment_request_view import (
    appointment_request_page,
    appointment_success,
)
from ophthalmology_portal.Core.views.home_page_view import HomePageView
from ophthalmology_portal.Core.views.log_in_view import (
    LogInView,
    PatientRegistrationView,
    RegistrationView,
)

__all__ = [
    "HomePageView",
    "LogInView",
    "RegistrationView",
    "PatientRegistrationView",
    "appointment_request_page",
    "appointment_success",
]
