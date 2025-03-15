from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import (
    ExamDoctorViewForm,
    ExamManagerViewForm,
    ExamPatientViewForm,
    OccularExamCreationForm,
    OccularExamViewForm,
    PrescriptionCreationForm,
    PrescriptionViewForm,
    VisualAccuityCreationForm,
    VisualAccuityViewForm,
)
from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView


class ExamDetailsView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if request.user.has_perm("Core.patient"):
            form = ExamPatientViewForm(instance=ExamModel.objects.get(id=exam_id))
            prescription_form = PrescriptionViewForm(
                instance=ExamModel.objects.get(id=exam_id).prescription
            )
            visual_form = VisualAccuityViewForm(
                instance=ExamModel.objects.get(id=exam_id).visual_accuity_information
            )
            occular_form = OccularExamViewForm(
                instance=ExamModel.objects.get(id=exam_id).occular_exam_information
            )
            return render(
                request,
                "view_exam.html",
                {
                    "form": form,
                    "base_template_name": self.get_base_template(request.user),
                    "prescription_form": prescription_form,
                    "visual_form": visual_form,
                    "occular_form": occular_form,
                    "upload": False,
                },
            )
        elif request.user.has_perm("Core.doctor"):
            form = ExamDoctorViewForm(instance=ExamModel.objects.get(id=exam_id))
            if ExamModel.objects.get(id=exam_id).status == "progressing":
                prescription_form = PrescriptionCreationForm
                visual_form = VisualAccuityCreationForm
                occular_form = OccularExamCreationForm
                return render(
                    request,
                    "view_exam.html",
                    {
                        "form": form,
                        "base_template_name": self.get_base_template(request.user),
                        "prescription_form": prescription_form,
                        "visual_form": visual_form,
                        "occular_form": occular_form,
                        "upload": True,
                    },
                )

            prescription_form = PrescriptionViewForm(
                instance=ExamModel.objects.get(id=exam_id).prescription
            )
            visual_form = VisualAccuityViewForm(
                instance=ExamModel.objects.get(id=exam_id).visual_accuity_information
            )
            occular_form = OccularExamViewForm(
                instance=ExamModel.objects.get(id=exam_id).occular_exam_information
            )
            return render(
                request,
                "view_exam.html",
                {
                    "form": form,
                    "base_template_name": self.get_base_template(request.user),
                    "prescription_form": prescription_form,
                    "visual_form": visual_form,
                    "occular_form": occular_form,
                    "upload": False,
                },
            )

        elif request.user.has_perm("Core.manager"):
            form = ExamManagerViewForm(instance=ExamModel.objects.get(id=exam_id))
            prescription_form = PrescriptionViewForm(
                instance=ExamModel.objects.get(id=exam_id).prescription
            )
            return render(
                request,
                "view_exam.html",
                {
                    "form": form,
                    "base_template_name": self.get_base_template(request.user),
                    "prescription_form": prescription_form,
                    "visual_form": visual_form,
                    "occular_form": occular_form,
                    "upload": False,
                },
            )

    def post(self, request: HttpRequest, exam_id, *args, **kwargs):
        form = VisualAccuityCreationForm(request.POST)
        form2 = OccularExamCreationForm(request.POST)
        form3 = PrescriptionCreationForm(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            exam = ExamModel.objects.get(id=exam_id)
            visual = form.save()
            occular = form2.save()
            prescription_temp = form3.save(commit=False)

            prescription_temp.prescriber = request.user.ophthalmologistusermodel
            prescription_temp.save()
            exam.visual_accuity_information = visual
            exam.occular_exam_information = occular
            exam.prescription = prescription_temp
            exam.save()
            return redirect(reverse("home_page"))
        return redirect(reverse("exam_details", kwargs={"exam_id": exam_id}))
