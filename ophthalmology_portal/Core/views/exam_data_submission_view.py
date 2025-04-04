from django.http import Http404, HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import (
    BothVisualAccuityCreationForm,
    IndividualVisualAccuityCreationForm,
    OccularExamCreationForm,
    OccularExamViewForm,
    VisualAccuityViewForm,
)
from ophthalmology_portal.Core.forms.exam_creation_form import ExamDoctorViewForm
from ophthalmology_portal.Core.forms.prescription_creation_form import (
    PrescriptionCreationForm,
    PrescriptionViewForm,
)
from ophthalmology_portal.Core.models.exam_model import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView


class TestInformationCreationView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        form = ExamDoctorViewForm(instance=ExamModel.objects.get(id=exam_id))
        if ExamModel.objects.get(id=exam_id).status == "Exam In Progress":
            prescription_form = PrescriptionCreationForm
            occular_form = OccularExamCreationForm
            if "HX-target" in request.headers:

                try:
                    request.GET['both']
                    visual_form = BothVisualAccuityCreationForm
                except:
                    visual_form = IndividualVisualAccuityCreationForm
                template = "visual_submission_template.html"
            else:
                template = "exam_data_submission.html"
                visual_form = IndividualVisualAccuityCreationForm
            return render(
                request,
                template,
                {
                    "form": form,
                    "base_template_name": self.get_base_template(request.user),
                    "prescription_form": prescription_form,
                    "visual_form": visual_form,
                    "occular_form": occular_form,
                    "upload": True,
                    "exam_id": exam_id,
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

    def post(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        try:
            request.POST['both']
            both = True
        except:
            both=False
        if both:
            form = BothVisualAccuityCreationForm(request.POST)
            form2 = OccularExamCreationForm(request.POST, request.FILES)
            form3 = PrescriptionCreationForm(request.POST)
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                visual=form.save(commit=False)
                exam = ExamModel.objects.get(id=exam_id)
                visual.visual_acuity_measure_left = visual.visual_acuity_measure_both
                visual.visual_acuity_measure_right = visual.visual_acuity_measure_both
                visual.corrector_indicator_left = visual.corrector_indicator_both
                visual.corrector_indicator_right = visual.corrector_indicator_both
                visual.pinhole_left = visual.pinhole_both
                visual.pinhole_right = visual.pinhole_both
                visual.save()

                prescription_temp = form3.save(commit=False)
                prescription_temp.prescriber = request.user.ophthalmologistusermodel
                prescription_temp.save()
                exam.visual_accuity_information = visual
                exam.occular_exam_information = form2.save()
                exam.prescription = prescription_temp
                exam.save()
                return redirect("/create-test-information/")
        else:
            form = IndividualVisualAccuityCreationForm(request.POST)
            form2 = OccularExamCreationForm(request.POST, request.FILES)
            form3 = PrescriptionCreationForm(request.POST)
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                form.save()
                form2.save()
                prescription_temp = form3.save(commit=False)
                prescription_temp.prescriber = request.user.ophthalmologistusermodel
                prescription_temp.save()
                exam.visual_accuity_information = visual
                exam.occular_exam_information = form2.save()
                exam.prescription = prescription_temp
                exam.save()
                return redirect("/create-test-information/")
        return redirect("/create-test-information/")
