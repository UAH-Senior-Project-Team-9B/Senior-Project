from ophthalmology_portal.Core.views.exam_creation_view import ExamCreationView
from ophthalmology_portal.Core.views.home_page_view import HomePageView
from ophthalmology_portal.Core.views.log_in_view import (
    LogInView,
    PatientRegistrationView,
    RegistrationView,
)
from ophthalmology_portal.Core.views.prescription_creation_view import (
    PrescriptionCreationView,
)
from ophthalmology_portal.Core.views.test_information_creation_view import (
    TestInformationCreationView,
)
from ophthalmology_portal.Core.views.patient_list_view import PatientListView
from ophthalmology_portal.Core.views.patient_history_view import PatientExamHistoryView
from ophthalmology_portal.Core.views.exam_details_view import ExamDetailsView
from ophthalmology_portal.Core.views.daily_exam_view import DailyExamsView

__all__ = [
    "HomePageView",
    "LogInView",
    "RegistrationView",
    "PatientRegistrationView",
    "ExamCreationView",
    "PrescriptionCreationView",
    "TestInformationCreationView",
    "PatientListView",
    "PatientExamHistoryView",
    "ExamDetailsView",
    "DailyExamsView"
]
