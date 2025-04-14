import datetime
import io
from zoneinfo import ZoneInfo

from django.http import FileResponse, Http404, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.platypus.tables import Table, TableStyle

from ophthalmology_portal.Core.forms import (
    ExamViewForm,
    OccularExamViewForm,
    PrescriptionViewForm,
)
from ophthalmology_portal.Core.forms.exam_creation_form import (
    ExamPatientViewNonCompleteForm,
    ExamTimeForm,
)
from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView


class RescheduleExam(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404
        exam = ExamModel.objects.get(id=exam_id)
        options = {
            f"{datetime.time(8)}": "8:00 AM",
            f"{datetime.time(8, 30)}": "8:30 AM",
            f"{datetime.time(9)}": "9:00 AM",
            f"{datetime.time(9, 30)}": "9:30 AM",
            f"{datetime.time(10)}": "10:00 AM",
            f"{datetime.time(10, 30)}": "10:30 AM",
            f"{datetime.time(11)}": "11:00 AM",
            f"{datetime.time(11, 30)}": "11:30 AM",
            f"{datetime.time(12)}": "12:00 PM",
            f"{datetime.time(12, 30)}": "12:30 PM",
            f"{datetime.time(13)}": "1:00 PM",
            f"{datetime.time(13, 30)}": "1:30 PM",
            f"{datetime.time(14)}": "2:00 PM",
            f"{datetime.time(14, 30)}": "2:30 PM",
            f"{datetime.time(15)}": "3:00 PM",
            f"{datetime.time(15, 30)}": "3:30 PM",
            f"{datetime.time(16)}": "4:00 PM",
            f"{datetime.time(16, 30)}": "4:30 PM",
            f"{datetime.time(17)}": "5:00 PM",
        }
        if request.user.has_perm("Core.manager"):
            if exam.status == ExamModel.status_choices["upcoming"]:
                form = ExamPatientViewNonCompleteForm(instance=exam)
                minimum = datetime.datetime.now(
                    ZoneInfo("America/Indiana/Knox")
                ).date() + datetime.timedelta(days=2)
                maximum = datetime.datetime.now(
                    ZoneInfo("America/Indiana/Knox")
                ).date() + datetime.timedelta(days=2 * 365)
                minimum = minimum.strftime("%Y-%m-%d")
                maximum = maximum.strftime("%Y-%m-%d")
                if "HX-target" in request.headers:
                    template_name = "time_submission.html"
                    if not request.GET["date"]:
                        pass
                    else:
                        already_taken = ExamModel.objects.filter(
                            date=request.GET["date"], doctor=exam.doctor
                        )
                        for i in already_taken:
                            options.pop(f"{i.time}")
                else:
                    template_name = "reschedule_exam.html"
                    already_taken = ExamModel.objects.filter(
                        date=datetime.datetime.now(
                            ZoneInfo("America/Indiana/Knox")
                        ).date(),
                        doctor=exam.doctor,
                    )
                    for i in already_taken:
                        options.pop(f"{i.time}")
                return render(
                    request,
                    template_name,
                    {
                        "form": form,
                        "base_template_name": self.get_base_template(request.user),
                        "upload": False,
                        "options": options,
                        "exam_id": exam_id,
                        "minimum": minimum,
                        "maximum": maximum,
                        "exam": exam,
                    },
                )
