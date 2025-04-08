from django.http import Http404, HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import (
    VisualAccuitySubmissionForm,
    OccularExamCreationForm,
    OccularExamViewForm,
    VisualAccuityViewForm,
)
from django.contrib.messages import get_messages
from ophthalmology_portal.Core.forms.exam_creation_form import ExamDoctorViewForm
from ophthalmology_portal.Core.forms.prescription_creation_form import (
    PrescriptionCreationForm,
    PrescriptionViewForm,
)
from ophthalmology_portal.Core.models.exam_model import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView
from django.contrib import messages

class TestInformationCreationView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        form = ExamDoctorViewForm(instance=ExamModel.objects.get(id=exam_id))

        if ExamModel.objects.get(id=exam_id).status == "Exam In Progress":
            prescription_form = PrescriptionCreationForm
            occular_form = OccularExamCreationForm
            aided_near = VisualAccuitySubmissionForm(prefix="aided_near")
            unaided_near = VisualAccuitySubmissionForm(prefix="unaided_near")
            pinhole_aided_near = VisualAccuitySubmissionForm(prefix="aided_ph_near")
            pinhole_unaided_near = VisualAccuitySubmissionForm(prefix="unaided_ph_near")
            aided_distance = VisualAccuitySubmissionForm(prefix="aided_distance")
            unaided_distance = VisualAccuitySubmissionForm(prefix="unaided_distance")
            pinhole_aided_distance = VisualAccuitySubmissionForm(prefix="aided_ph_distance")
            pinhole_unaided_distance = VisualAccuitySubmissionForm(prefix="unaided_ph_distance")
            return render(
                request,
                "exam_data_submission.html",
                {
                    "form": form,
                    "base_template_name": self.get_base_template(request.user),
                    "prescription_form": prescription_form,
                    "occular_form": occular_form,
                    "upload": True,
                    "exam_id": exam_id,
                    "aided_near": aided_near,
                    "unaided_near": unaided_near,
                    "aided_ph_near": pinhole_aided_near,
                    "unaided_ph_near": pinhole_unaided_near,
                    "aided_distance": aided_distance,
                    "unaided_distance": unaided_distance,
                    "aided_ph_distance": pinhole_aided_distance,
                    "unaided_ph_distance": pinhole_unaided_distance,
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
        aided_near = VisualAccuitySubmissionForm(request.POST, prefix="aided_near")
        unaided_near = VisualAccuitySubmissionForm(request.POST, prefix="unaided_near")
        # aided_near = aided_near.save(commit=False)
        # unaided_near = unaided_near.save(commit=False)
        pinhole_aided_near = VisualAccuitySubmissionForm(request.POST, prefix="aided_ph_near")
        pinhole_unaided_near = VisualAccuitySubmissionForm(request.POST, prefix="unaided_ph_near")
        aided_distance = VisualAccuitySubmissionForm(request.POST, prefix="aided_distance")
        unaided_distance = VisualAccuitySubmissionForm(request.POST, prefix="unaided_near_distance")
        # aided_distance = aided_distance.save(commit=False)
        # unaided_distance = unaided_distance.save(commit=False)
        pinhole_aided_distance = VisualAccuitySubmissionForm(request.POST, prefix="aided_ph_distance")
        pinhole_unaided_distance = VisualAccuitySubmissionForm(request.POST, prefix="unaided_ph_distance")
        form2 = OccularExamCreationForm(request.POST, request.FILES)
        form3 = PrescriptionCreationForm(request.POST)
        if (aided_near.is_valid() and form2.is_valid() and form3.is_valid() and unaided_near.is_valid() and pinhole_aided_near.is_valid() and pinhole_unaided_near.is_valid()
            and aided_distance.is_valid() and unaided_distance.is_valid() and pinhole_aided_distance.is_valid() and pinhole_unaided_distance.is_valid()):
            aided_near = aided_near.save(commit=False)
            unaided_near = unaided_near.save(commit=False)
            pinhole_aided_near = pinhole_aided_near.save(commit=False)
            pinhole_unaided_near = pinhole_unaided_near.save(commit=False)
            _validate_accuity(request, unaided_near, pinhole_unaided_near)
            _validate_accuity(request, aided_near, pinhole_aided_near)
            aided_distance = aided_distance.save(commit=False)
            unaided_distance = unaided_distance.save(commit=False)
            pinhole_aided_distance = pinhole_aided_distance.save(commit=False)
            pinhole_unaided_distance = pinhole_unaided_distance.save(commit=False)
            _validate_accuity(request, aided_distance, pinhole_aided_distance)
            _validate_accuity(request, pinhole_aided_distance, pinhole_unaided_distance)
            storage = get_messages(request)
            for i in storage:
                if i:
                    storage.used=False
                    return redirect(reverse("exam_data_submission", kwargs={"exam_id": exam_id}))

            aided_near.save()
            unaided_near.save()
            pinhole_aided_near.save()
            pinhole_unaided_near.save()
            aided_distance.save()
            unaided_distance.save()
            pinhole_aided_distance.save()
            pinhole_unaided_distance.save()
            form2 = OccularExamCreationForm(request.POST, request.FILES)
            form3 = PrescriptionCreationForm(request.POST)
            exam = ExamModel.objects.get(id=exam_id)

            exam.visual_accuity_aided_near = aided_near
            exam.visual_accuity_unaided_near = unaided_near
            exam.visual_accuity_pinhole_unaided_near = pinhole_unaided_near
            exam.visual_accuity_pinhole_aided_near = pinhole_aided_near
            exam.visual_accuity_aided_distance = aided_distance
            exam.visual_accuity_unaided_distance = unaided_distance
            exam.visual_accuity_pinhole_aided_distance = pinhole_aided_distance
            exam.visual_accuity_pinhole_unaided_distance = pinhole_unaided_distance

            prescription_temp = form3.save(commit=False)
            prescription_temp.prescriber = request.user.ophthalmologistusermodel
            prescription_temp.save()
            exam.occular_exam_information = form2.save()
            exam.prescription = prescription_temp
            exam.save()
            return redirect(reverse("exam_details", kwargs={"exam_id": exam_id}))


def _validate_accuity(request, parent, child):

    if child.visual_acuity_measure_left and not parent.visual_acuity_measure_left:

        messages.add_message(request, messages.ERROR, "Left eye values do not match")
    if child.visual_acuity_measure_right and not parent.visual_acuity_measure_right:
        messages.add_message(request, messages.ERROR, "Right eye values do not match")
    if child.visual_acuity_measure_both and not parent.visual_acuity_measure_both:
        messages.add_message(request, messages.ERROR, "Both eye values do not match")
