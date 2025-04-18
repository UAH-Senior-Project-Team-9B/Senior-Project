from ophthalmology_portal.Core.views.cancel_exam import CancelExam
from ophthalmology_portal.Core.views.daily_exam_view import DailyExamsView
from ophthalmology_portal.Core.views.exam_confirmation_view import ExamConfirmationView
from ophthalmology_portal.Core.views.exam_confirmations_view import (
    ExamConfirmationsView,
)
from ophthalmology_portal.Core.views.exam_creation_view import (
    ExamCreationView,
)
from ophthalmology_portal.Core.views.exam_data_submission_view import (
    TestInformationCreationView,
)
from ophthalmology_portal.Core.views.exam_details_view import (
    ExamDetailsView,
    PrescriptionPDF,
    PrescriptionPrintPDF,
)
from ophthalmology_portal.Core.views.exam_request_view import PatientExamCreationView
from ophthalmology_portal.Core.views.home_page_view import HomePageView
from ophthalmology_portal.Core.views.log_in_view import (
    LogInView,
    LogOutView,
    PatientInformationRegistrationView,
    RegistrationView,
)
from ophthalmology_portal.Core.views.patient_history_view import PatientExamHistoryView
from ophthalmology_portal.Core.views.patient_information_view import (
    PatientInformationOtherView,
    PatientInformationView,
)
from ophthalmology_portal.Core.views.patient_list_view import PatientListView
from ophthalmology_portal.Core.views.prescription_creation_view import (
    PrescriptionCreationView,
)
from ophthalmology_portal.Core.views.prescription_list_view import PrescriptionListView
from ophthalmology_portal.Core.views.progress_exam import (
    ProgressExam,
    RegressExam,
)
from ophthalmology_portal.Core.views.reschedule_exam import RescheduleExam

__all__ = [
    "HomePageView",
    "LogInView",
    "RegistrationView",
    "PatientInformationRegistrationView",
    "ExamCreationView",
    "PrescriptionCreationView",
    "TestInformationCreationView",
    "PatientListView",
    "PatientExamHistoryView",
    "ExamDetailsView",
    "DailyExamsView",
    "PatientExamCreationView",
    "PatientInformationView",
    "ExamConfirmationsView",
    "ExamConfirmationView",
    "LogOutView",
    "PrescriptionListView",
    "PrescriptionPDF",
    "PrescriptionPrintPDF",
    "PatientInformationOtherView",
    "CancelExam",
    "ProgressExam",
    "RegressExam",
    "PatientInformationOtherView",
    "RescheduleExam",
    "RegressExam",
]
