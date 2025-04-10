import io
from zoneinfo import ZoneInfo
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from reportlab.platypus.tables import Table, TableStyle
from ophthalmology_portal.Core.forms import (
    ExamManagerViewForm,
    ExamViewForm,
    OccularExamCreationForm,
    OccularExamViewForm,
    PrescriptionCreationForm,
    PrescriptionViewForm,
    VisualAccuityViewForm,
)
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from ophthalmology_portal.Core.forms.exam_creation_form import ExamArrivalForm, ExamManagerArrivalTimeForm, ExamPatientViewNonCompleteForm, ExamTimeForm
from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView
from django.http import Http404
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

import datetime
from django.http import FileResponse

class PrescriptionPDF(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        elements = []
        exam=ExamModel.objects.get(id=exam_id)
        buffer = io.BytesIO()
        canv = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
        textob = canv.beginText()
        textob.setTextOrigin(inch,inch)
        # for line in lines:
        #     textob.textLine(line)
        # canv.drawText(textob)
        # elements.append(textob)
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        presc = exam.prescription
        name = f"{exam.patient}"

        max_len = 100
        white_space = "&nbsp;"
        for i in range(0, (max_len-len(name))):
            white_space = white_space + "&nbsp;"
        elements.append(Paragraph(f"Patient: <u>{exam.patient}{white_space}</u> Issued: <u>{presc.date_prescribed}</u>"))
        elements.append(Spacer(1,1/4*inch))
        data = [["", "Rx", "SPH", "CYL", "AXIS", "PRISM", "BASE"],
                ["Distance","O.D.", f"{presc.od_sphere}", f"{presc.od_cylinder}", f"{presc.od_axis}", f"{presc.od_prism}", f"{presc.od_prism_base}"],
                ["","O.S.", f"{presc.os_sphere}", f"{presc.os_cylinder}", f"{presc.os_axis}", f"{presc.os_prism}", f"{presc.os_prism_base}"],
                ["ADD","O.D.", f"{presc.od_add}", "","","", ""],
                ["","O.S.",f"{presc.os_add}","","", "", ""]]
        table = Table(data)
        table.setStyle(TableStyle([
            ('GRID',(1,0),(6,2),1,colors.black),
            ('GRID',(0,1),(2,5),1,colors.black),
            ('SPAN',(0,1),(0,2)),
            ('SPAN',(0,3),(0,4)),
            ('SPAN',(3,3),(-1,-1)),
            ]))
        elements.append(table)
        elements.append(Spacer(1,1/4*inch))
        name = f"{presc.prescriber}"
        max_len = 130
        white_space = "&nbsp;"
        for i in range(0, (max_len-len(name))):
            white_space = white_space + "&nbsp;"
        elements.append(Paragraph(f"Prescriber: <u>{name}{white_space}</u>"))
        doc.build(elements)
        # width = 400
        # height = 100
        # x = 100
        # y = 400
        # table.wrapOn(canv, width, height)
        # table.drawOn(canv, x, y)
        # canv.save()
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
        if request.user.has_perm("Core.doctor"):

            if exam.status == ExamModel.status_choices['complete']:
                form = ExamViewForm(instance=exam)
                occular_form = OccularExamViewForm(
                    instance=exam.occular_exam_information
                )
                prescription_form = PrescriptionViewForm(
                    instance=exam.prescription
                )
            else:
                form = ExamPatientViewNonCompleteForm(instance=exam)
                occular_form = None
                prescription_form = None

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
                    "exam": exam,
                    "occular_form": occular_form,
                    "upload": False,
                },
            )
        if request.user.has_perm("Core.patient"):

            if exam.status == ExamModel.status_choices['complete']:
                form = ExamViewForm(instance=exam)
                occular_form = OccularExamViewForm(
                    instance=exam.occular_exam_information
                )
                prescription_form = PrescriptionViewForm(
                    instance=exam.prescription
                )
            else:
                form = ExamPatientViewNonCompleteForm(instance=exam)
                occular_form = None
                prescription_form = None

            if exam.status == ExamModel.status_choices['upcoming']:
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
                    "exam": exam,
                    "occular_form": occular_form,
                    "upload": False,
                },
            )

        elif request.user.has_perm("Core.manager"):



            if exam.prescription:
                prescription_form = PrescriptionViewForm(
                    instance=exam.prescription
                )
            else:
                prescription_form= None

            if exam.status==ExamModel.status_choices['upcoming']:
                form = ExamPatientViewNonCompleteForm(instance=exam)
                if exam.date == datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date():
                    stageable = True
                else:
                    stageable = False
                minimum = datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() + datetime.timedelta(days=2)
                maximum = datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() + datetime.timedelta(days=2 * 365)
                minimum = minimum.strftime("%Y-%m-%d")
                maximum = maximum.strftime("%Y-%m-%d")
                cancellable = True
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
            elif exam.status == ExamModel.status_choices['waiting']:
                form = ExamPatientViewNonCompleteForm(instance=exam)
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
                form = ExamViewForm(instance=exam)
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
        try:
            request.POST['time']
            reschedule = True
        except:
            reschedule = False
        if reschedule:
            form = ExamTimeForm(request.POST, instance=exam)
            if form.is_valid():
                form.save()

        return redirect(reverse("exam_details", kwargs={"exam_id": exam_id}))
