import datetime
import io

from django.http import FileResponse, Http404, HttpRequest
from django.shortcuts import redirect, render
from django.urls import resolve, reverse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.platypus.tables import Table, TableStyle
from zoneinfo import ZoneInfo
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
from ophthalmology_portal.Core.models.user_models import PatientUserModel
from ophthalmology_portal.Core.views.base_view import BaseView


class PrescriptionPDF(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if request.user.has_perm("Core.patient"):
            try:
                exam = ExamModel.objects.get(
                    id=exam_id, patient=PatientUserModel.objects.get(user=request.user)
                )
            except:
                raise Http404
        elements = []
        exam = ExamModel.objects.get(id=exam_id)
        buffer = io.BytesIO()
        canv = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
        textob = canv.beginText()
        textob.setTextOrigin(inch, inch)
        # for line in lines:
        #     textob.textLine(line)
        # canv.drawText(textob)
        # elements.append(textob)
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        presc = exam.prescription
        name = f"{exam.patient}"

        max_len = 100
        white_space = "&nbsp;"
        for i in range(0, (max_len - len(name))):
            white_space = white_space + "&nbsp;"
        elements.append(
            Paragraph(
                f"Patient: <u>{exam.patient}{white_space}</u> Issued: <u>{presc.date_prescribed}</u>"
            )
        )
        elements.append(Spacer(1, 1 / 4 * inch))
        data = [
            ["", "Rx", "SPH", "CYL", "AXIS", "PRISM", "BASE"],
            [
                "Distance",
                "O.D.",
                f"{presc.od_sphere}",
                f"{presc.od_cylinder}",
                f"{presc.od_axis}",
                f"{presc.od_prism}",
                f"{presc.od_prism_base}",
            ],
            [
                "",
                "O.S.",
                f"{presc.os_sphere}",
                f"{presc.os_cylinder}",
                f"{presc.os_axis}",
                f"{presc.os_prism}",
                f"{presc.os_prism_base}",
            ],
            ["ADD", "O.D.", f"{presc.od_add}", "", "", "", ""],
            ["", "O.S.", f"{presc.os_add}", "", "", "", ""],
        ]
        table = Table(data)
        table.setStyle(
            TableStyle([
                ("GRID", (1, 0), (6, 2), 1, colors.black),
                ("GRID", (0, 1), (2, 5), 1, colors.black),
                ("SPAN", (0, 1), (0, 2)),
                ("SPAN", (0, 3), (0, 4)),
                ("SPAN", (3, 3), (-1, -1)),
            ])
        )
        elements.append(table)
        elements.append(Spacer(1, 1 / 4 * inch))
        name = f"{presc.prescriber}"
        max_len = 130
        white_space = "&nbsp;"
        for i in range(0, (max_len - len(name))):
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
        return FileResponse(
            buffer, as_attachment=True, filename=f"{exam.date}_prescription.pdf"
        )


class PrescriptionPrintPDF(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if request.user.has_perm("Core.patient"):
            try:
                exam = ExamModel.objects.get(
                    id=exam_id, patient=PatientUserModel.objects.get(user=request.user)
                )
            except:
                raise Http404
        else:
            exam = ExamModel.objects.get(id=exam_id)
        elements = []
        buffer = io.BytesIO()
        canv = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
        textob = canv.beginText()
        textob.setTextOrigin(inch, inch)
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        presc = exam.prescription
        name = f"{exam.patient}"

        max_len = 100
        white_space = "&nbsp;"
        for i in range(0, (max_len - len(name))):
            white_space = white_space + "&nbsp;"
        elements.append(
            Paragraph(
                f"Patient: <u>{exam.patient}{white_space}</u> Issued: <u>{presc.date_prescribed}</u>"
            )
        )
        elements.append(Spacer(1, 1 / 4 * inch))
        data = [
            ["", "Rx", "SPH", "CYL", "AXIS", "PRISM", "BASE"],
            [
                "Distance",
                "O.D.",
                f"{presc.od_sphere}",
                f"{presc.od_cylinder}",
                f"{presc.od_axis}",
                f"{presc.od_prism}",
                f"{presc.od_prism_base}",
            ],
            [
                "",
                "O.S.",
                f"{presc.os_sphere}",
                f"{presc.os_cylinder}",
                f"{presc.os_axis}",
                f"{presc.os_prism}",
                f"{presc.os_prism_base}",
            ],
            ["ADD", "O.D.", f"{presc.od_add}", "", "", "", ""],
            ["", "O.S.", f"{presc.os_add}", "", "", "", ""],
        ]
        table = Table(data)
        table.setStyle(
            TableStyle([
                ("GRID", (1, 0), (6, 2), 1, colors.black),
                ("GRID", (0, 1), (2, 5), 1, colors.black),
                ("SPAN", (0, 1), (0, 2)),
                ("SPAN", (0, 3), (0, 4)),
                ("SPAN", (3, 3), (-1, -1)),
            ])
        )
        elements.append(table)
        elements.append(Spacer(1, 1 / 4 * inch))
        name = f"{presc.prescriber}"
        max_len = 130
        white_space = "&nbsp;"
        for i in range(0, (max_len - len(name))):
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
        return FileResponse(
            buffer,
            as_attachment=False,
            filename=f"{exam.date}_prescription.pdf",
            content_type="application/pdf",
        )


class ExamDetailsView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
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
            exam = ExamModel.objects.get(id=exam_id)
            form = ExamPatientViewNonCompleteForm(instance=exam)

            occular_form = None
            prescription_form = None
            if exam.status == ExamModel.status_choices["complete"]:
                form = ExamViewForm(instance=exam)
                occular_form = OccularExamViewForm(
                    instance=exam.occular_exam_information
                )
                prescription_form = PrescriptionViewForm(instance=exam.prescription)
            else:
                if exam.status == ExamModel.status_choices["postexam"]:
                    form = ExamViewForm(instance=exam)
                    occular_form = OccularExamViewForm(
                        instance=exam.occular_exam_information
                    )
                    prescription_form = PrescriptionViewForm(instance=exam.prescription)

            return render(
                request,
                "exam_details.html",
                {
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
            if resolve(request.path_info).url_name == "daily_exam_instance":
                raise Http404
            try:
                exam = ExamModel.objects.get(
                    id=exam_id, patient=PatientUserModel.objects.get(user=request.user)
                )
            except:
                raise Http404
            if (
                exam.status == ExamModel.status_choices["complete"]
                or exam.status == ExamModel.status_choices["postexam"]
            ):
                form = ExamViewForm(instance=exam)
                occular_form = OccularExamViewForm(
                    instance=exam.occular_exam_information
                )
                prescription_form = PrescriptionViewForm(instance=exam.prescription)
            else:
                form = ExamPatientViewNonCompleteForm(instance=exam)
                occular_form = None
                prescription_form = None

            return render(
                request,
                "exam_details.html",
                {
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
            exam = ExamModel.objects.get(id=exam_id)
            today = datetime.datetime.now(ZoneInfo('America/Indiana/Knox')).date()
            if exam.prescription:
                prescription_form = PrescriptionViewForm(instance=exam.prescription)
            else:
                prescription_form = None

            if (
                exam.status == ExamModel.status_choices["postexam"]
                or exam.status == ExamModel.status_choices["complete"]
            ):
                form = ExamViewForm(instance=exam)
                return render(
                    request,
                    "exam_details.html",
                    {
                        "form": form,
                        "base_template_name": self.get_base_template(request.user),
                        "prescription_form": prescription_form,
                        "upload": False,
                        "exam_id": exam_id,
                        "exam": exam,
                    },
                )
            else:
                form = ExamPatientViewNonCompleteForm(instance=exam)
                return render(
                    request,
                    "exam_details.html",
                    {
                        "form": form,
                        "base_template_name": self.get_base_template(request.user),
                        "prescription_form": prescription_form,
                        "upload": False,
                        "exam_id": exam_id,
                        "exam": exam,
                        "today": today,
                    },
                )

    def post(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404
        exam = ExamModel.objects.get(id=exam_id)
        try:
            request.POST["time"]
            reschedule = True
        except:
            reschedule = False
            # Duct Tape
            try:
                if request.POST[f"{exam_id}"] == "Deny":
                    instance = ExamModel.objects.get(id=exam_id)
                    instance.delete()
                elif request.POST[f"{exam_id}"] == "Confirm":
                    instance = ExamModel.objects.get(id=exam_id)
                    instance.status = ExamModel.status_choices["upcoming"]
                    instance.save()
                return redirect("/exam-confirmations/")
            except:
                reschedule = False
        if reschedule:
            form = ExamTimeForm(request.POST, instance=exam)
            if form.is_valid():
                form.save()

        return redirect(reverse("exam_details", kwargs={"exam_id": exam_id}))
