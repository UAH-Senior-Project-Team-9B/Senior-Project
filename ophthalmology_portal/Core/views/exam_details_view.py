from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import (
    ExamManagerViewForm,
    ExamPatientViewForm,
    OccularExamCreationForm,
    OccularExamViewForm,
    PrescriptionCreationForm,
    PrescriptionViewForm,
    VisualAccuityViewForm,
)
from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView
from django.http import Http404

class ExamDetailsView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if request.user.has_perm("Core.patient") or request.user.has_perm("Core.doctor"):
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
                "exam_details.html",
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
                "exam_details.html",
                {
                    "form": form,
                    "base_template_name": self.get_base_template(request.user),
                    "prescription_form": prescription_form,
                    "upload": False,
                },
            )

    def post(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404
        return redirect(reverse("exam_details", kwargs={"exam_id": exam_id}))
