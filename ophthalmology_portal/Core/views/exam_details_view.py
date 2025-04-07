import io
from zoneinfo import ZoneInfo
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from reportlab.platypus.tables import Table, TableStyle
from ophthalmology_portal.Core.forms import (
    ExamManagerViewForm,
    ExamPatientViewForm,
    OccularExamCreationForm,
    OccularExamViewForm,
    PrescriptionCreationForm,
    PrescriptionViewForm,
    VisualAccuityViewForm,
)
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from ophthalmology_portal.Core.forms.exam_creation_form import ExamArrivalForm, ExamManagerArrivalTimeForm, ExamTimeForm
from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView
from django.http import Http404
import datetime
from django.http import FileResponse

class PrescriptionPDF(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        exam=ExamModel.objects.get(id=exam_id)
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []
        presc = exam.prescription
        data = [["Rx", "SPH", "CYL", "AXIS", "PRISM", "BASE"],
                ["O.D.", f"{presc.od_sphere}", f"{presc.od_cylinder}", f"{presc.od_axis}", f"{presc.od_prism}", f"{presc.od_prism_base}"],
                ["O.S.", f"{presc.os_sphere}", f"{presc.os_cylinder}", f"{presc.os_axis}", f"{presc.os_prism}", f"{presc.os_prism_base}"],
                ["ADD","","","","O.D.", f"{presc.od_add}"],
                ["","","","","O.S.", f"{presc.os_add}"]]
        table = Table(data)
        table.setStyle(TableStyle([('GRID',(0,0),(6,5),1,colors.black), ('SPAN',(0,3),(3,4))]))
        elements.append(table)
        doc.build(elements)
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f"{exam.date}_prescription.pdf")


class ExamDetailsView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):

        exam=ExamModel.objects.get(id=exam_id)
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
        if request.user.has_perm("Core.patient") or request.user.has_perm("Core.doctor"):
            form = ExamPatientViewForm(instance=exam)
            prescription_form = PrescriptionViewForm(
                instance=exam.prescription
            )
            visual_form = VisualAccuityViewForm(
                instance=exam.visual_accuity_information
            )
            occular_form = OccularExamViewForm(
                instance=exam.occular_exam_information
            )
            if exam.status == "Upcoming":
                    cancellable = True
            else:
                cancellable = False
            return render(
                request,
                "exam_details.html",
                {
                    "cancellable": cancellable,
                    "form": form,
                    "exam_id": exam_id,
                    "base_template_name": self.get_base_template(request.user),
                    "prescription_form": prescription_form,
                    "visual_form": visual_form,
                    "occular_form": occular_form,
                    "upload": False,
                },
            )

        elif request.user.has_perm("Core.manager"):

            form = ExamManagerViewForm(instance=exam)

            if exam.prescription:
                prescription_form = PrescriptionViewForm(
                    instance=exam.prescription
                )
            else:
                prescription_form= None

            if exam.status=="Upcoming":
                if exam.date == datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date():
                    form = ExamManagerArrivalTimeForm(instance=exam)
                breakpoint()
                minimum = datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() + datetime.timedelta(days=2)
                maximum = datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() + datetime.timedelta(days=2 * 365)
                minimum = minimum.strftime("%Y-%m-%d")
                maximum = maximum.strftime("%Y-%m-%d")
                cancellable = True
                stageable = False
                if "HX-target" in request.headers:
                    template_name = "time_submission.html"
                    if not request.GET["date"]:
                        pass
                    else:
                        already_taken = ExamModel.objects.filter(date=request.GET["date"], doctor=exam.doctor)
                        for i in already_taken:
                            options.pop(f"{i.time}")
                else:
                    template_name = "exam_details_manager_update.html"
                    already_taken = ExamModel.objects.filter(
                            date=datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date(),
                            doctor=exam.doctor
                        )
                    for i in already_taken:
                        options.pop(f"{i.time}")
                return render(
                    request,
                    template_name,
                    {
                        "stageable": stageable,
                        "cancellable": cancellable,
                        "form": form,
                        "base_template_name": self.get_base_template(request.user),
                        "prescription_form": prescription_form,
                        "upload": False,
                        "options": options,
                        "exam_id": exam_id,
                        "minimum": minimum,
                        "maximum": maximum,
                    },
                )
            elif exam.status=="Exam In Progress" or exam.status == "In Wait Room":
                breakpoint()
                cancellable = True
                stageable = True
                return render(
                    request,
                    "exam_details.html",
                    {
                        "stageable": stageable,
                        "cancellable": cancellable,
                        "form": form,
                        "base_template_name": self.get_base_template(request.user),
                        "prescription_form": prescription_form,
                        "upload": False,
                        "exam_id": exam_id,
                    },
                )
            else:
                breakpoint()
                cancellable = False
                stageable = False
                return render(
                    request,
                    "exam_details.html",
                    {
                        "stageable": stageable,
                        "cancellable": cancellable,
                        "form": form,
                        "base_template_name": self.get_base_template(request.user),
                        "prescription_form": prescription_form,
                        "upload": False,
                        "exam_id": exam_id,
                    },
                )

    def post(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404
        exam=ExamModel.objects.get(id=exam_id)
        breakpoint()
        try:
            request.POST['time']
            reschedule = True
        except:
            reschedule = False
        try:
            request.POST['arrival_time']
            update = True
        except:
             update = False
        if reschedule:
            form = ExamTimeForm(request.POST, instance=exam)
            if form.is_valid():
                form.save()
        if update:
            form = ExamArrivalForm(request.POST, instance=exam)
            if form.is_valid():
                form.save()
                exam.in_lobby()

        return redirect(reverse("exam_details", kwargs={"exam_id": exam_id}))
