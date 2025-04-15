from django.contrib import messages
from django.contrib.messages import get_messages
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import (
    OccularExamCreationForm,
    OccularExamViewForm,
    PatientUserUpdateForm,
    VisualAccuitySubmissionForm,
)
from ophthalmology_portal.Core.forms.exam_creation_form import ExamDoctorViewForm
from ophthalmology_portal.Core.forms.patient_info_form import TreatmentForm
from ophthalmology_portal.Core.forms.prescription_creation_form import (
    PrescriptionCreationForm,
    PrescriptionViewForm,
)
from ophthalmology_portal.Core.models.exam_model import ExamModel
from ophthalmology_portal.Core.models.user_models import (
    OphthalmologistUserModel,
    PatientUserModel,
)
from ophthalmology_portal.Core.views.base_view import BaseView


class TestInformationCreationView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        form = ExamDoctorViewForm(instance=ExamModel.objects.get(id=exam_id))
        user = OphthalmologistUserModel.objects.get(user=request.user)
        patient = PatientUserModel.objects.get(id=form.instance.patient.id)
        treatment = TreatmentForm(instance=patient)
        try:
            exam = ExamModel.objects.get(id=exam_id, doctor=user)
        except:
            raise Http404
        if (
            exam.status == ExamModel.status_choices["progressing"]
            or exam.status == ExamModel.status_choices["postexam"]
        ):
            prescription_form = PrescriptionCreationForm(instance=exam.prescription)
            occular_form = OccularExamCreationForm(
                instance=exam.occular_exam_information
            )
            aided_near = VisualAccuitySubmissionForm(
                instance=exam.visual_accuity_aided_near, prefix="aided_near"
            )
            unaided_near = VisualAccuitySubmissionForm(
                instance=exam.visual_accuity_unaided_near, prefix="unaided_near"
            )
            pinhole_aided_near = VisualAccuitySubmissionForm(
                instance=exam.visual_accuity_pinhole_aided_near, prefix="aided_ph_near"
            )
            pinhole_unaided_near = VisualAccuitySubmissionForm(
                instance=exam.visual_accuity_pinhole_unaided_near,
                prefix="unaided_ph_near",
            )
            aided_distance = VisualAccuitySubmissionForm(
                instance=exam.visual_accuity_aided_distance, prefix="aided_distance"
            )
            unaided_distance = VisualAccuitySubmissionForm(
                instance=exam.visual_accuity_unaided_distance, prefix="unaided_distance"
            )
            pinhole_aided_distance = VisualAccuitySubmissionForm(
                instance=exam.visual_accuity_pinhole_aided_distance,
                prefix="aided_ph_distance",
            )
            pinhole_unaided_distance = VisualAccuitySubmissionForm(
                instance=exam.visual_accuity_pinhole_unaided_distance,
                prefix="unaided_ph_distance",
            )

            return render(
                request,
                "exam_data_submission.html",
                {
                    "form": form,
                    "treatment": treatment,
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
        aided_near = VisualAccuitySubmissionForm(
            instance=exam.visual_accuity_aided_near, prefix="aided_near"
        )
        unaided_near = VisualAccuitySubmissionForm(
            instance=exam.visual_accuity_unaided_near, prefix="unaided_near"
        )
        pinhole_aided_near = VisualAccuitySubmissionForm(
            instance=exam.visual_accuity_pinhole_aided_near, prefix="aided_ph_near"
        )
        pinhole_unaided_near = VisualAccuitySubmissionForm(
            instance=exam.visual_accuity_pinhole_unaided_near,
            prefix="unaided_ph_near",
        )
        aided_distance = VisualAccuitySubmissionForm(
            instance=exam.visual_accuity_aided_distance, prefix="aided_distance"
        )
        unaided_distance = VisualAccuitySubmissionForm(
            instance=exam.visual_accuity_unaided_distance, prefix="unaided_distance"
        )
        pinhole_aided_distance = VisualAccuitySubmissionForm(
            instance=exam.visual_accuity_pinhole_aided_distance,
            prefix="aided_ph_distance",
        )
        pinhole_unaided_distance = VisualAccuitySubmissionForm(
            instance=exam.visual_accuity_pinhole_unaided_distance,
            prefix="unaided_ph_distance",
        )
        occular_form = OccularExamViewForm(
            instance=ExamModel.objects.get(id=exam_id).occular_exam_information
        )
        return render(
            request,
            "exam_details.html",
            {
                "form": form,
                "treatment": treatment,
                "base_template_name": self.get_base_template(request.user),
                "prescription_form": prescription_form,
                "exam_id": exam_id,
                "aided_near": aided_near,
                "unaided_near": unaided_near,
                "aided_ph_near": pinhole_aided_near,
                "unaided_ph_near": pinhole_unaided_near,
                "aided_distance": aided_distance,
                "unaided_distance": unaided_distance,
                "aided_ph_distance": pinhole_aided_distance,
                "unaided_ph_distance": pinhole_unaided_distance,
                "occular_form": occular_form,
                "upload": False,
            },
        )

    def post(self, request: HttpRequest, exam_id, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        form = ExamDoctorViewForm(instance=ExamModel.objects.get(id=exam_id))
        user = OphthalmologistUserModel.objects.get(user=request.user)
        try:
            exam = ExamModel.objects.get(id=exam_id, doctor=user)
        except:
            raise Http404
        patient = PatientUserModel.objects.get(id=form.instance.patient.id)
        treatment = TreatmentForm(request.POST, instance=patient)
        aided_near = VisualAccuitySubmissionForm(request.POST, prefix="aided_near")
        unaided_near = VisualAccuitySubmissionForm(request.POST, prefix="unaided_near")
        pinhole_aided_near = VisualAccuitySubmissionForm(
            request.POST, prefix="aided_ph_near"
        )
        pinhole_unaided_near = VisualAccuitySubmissionForm(
            request.POST, prefix="unaided_ph_near"
        )
        aided_distance = VisualAccuitySubmissionForm(
            request.POST, prefix="aided_distance"
        )
        unaided_distance = VisualAccuitySubmissionForm(
            request.POST, prefix="unaided_distance"
        )
        pinhole_aided_distance = VisualAccuitySubmissionForm(
            request.POST, prefix="aided_ph_distance"
        )
        pinhole_unaided_distance = VisualAccuitySubmissionForm(
            request.POST, prefix="unaided_ph_distance"
        )
        occular_form = OccularExamCreationForm(request.POST, request.FILES)
        prescription_form = PrescriptionCreationForm(request.POST)
        patient_information_form = PatientUserUpdateForm(request.POST)

        if (
            aided_near.is_valid()
            and occular_form.is_valid()
            and prescription_form.is_valid()
            and unaided_near.is_valid()
            and pinhole_aided_near.is_valid()
            and pinhole_unaided_near.is_valid()
            and aided_distance.is_valid()
            and unaided_distance.is_valid()
            and pinhole_aided_distance.is_valid()
            and pinhole_unaided_distance.is_valid()
        ):
            aided_near_obj = aided_near.save(commit=False)
            unaided_near_obj = unaided_near.save(commit=False)
            pinhole_aided_near_obj = pinhole_aided_near.save(commit=False)
            pinhole_unaided_near_obj = pinhole_unaided_near.save(commit=False)
            _validate_accuity(
                request, unaided_near_obj, pinhole_unaided_near_obj, "unaided_near"
            )
            _validate_accuity(
                request, aided_near_obj, pinhole_aided_near_obj, "aided_near"
            )
            aided_distance_obj = aided_distance.save(commit=False)
            unaided_distance_obj = unaided_distance.save(commit=False)
            pinhole_aided_distance_obj = pinhole_aided_distance.save(commit=False)
            pinhole_unaided_distance_obj = pinhole_unaided_distance.save(commit=False)
            _validate_accuity(
                request,
                aided_distance_obj,
                pinhole_aided_distance_obj,
                "aided_distance",
            )
            _validate_accuity(
                request,
                unaided_distance_obj,
                pinhole_unaided_distance_obj,
                "unaided_distance",
            )
            storage = get_messages(request)
            for i in storage:
                if i:
                    storage.used = False
                    return render(
                        request,
                        "exam_data_submission.html",
                        {
                            "form": form,
                            "treatment": treatment,
                            "patient": patient_information_form,
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

            aided_near_obj.save()
            unaided_near_obj.save()
            pinhole_aided_near_obj.save()
            pinhole_unaided_near_obj.save()
            aided_distance_obj.save()
            unaided_distance_obj.save()
            pinhole_aided_distance_obj.save()
            pinhole_unaided_distance_obj.save()
            form2 = OccularExamCreationForm(request.POST, request.FILES)
            form3 = PrescriptionCreationForm(request.POST)
            exam = ExamModel.objects.get(id=exam_id)

            exam.visual_accuity_aided_near = aided_near_obj
            exam.visual_accuity_unaided_near = unaided_near_obj
            exam.visual_accuity_pinhole_unaided_near = pinhole_unaided_near_obj
            exam.visual_accuity_pinhole_aided_near = pinhole_aided_near_obj
            exam.visual_accuity_aided_distance = aided_distance_obj
            exam.visual_accuity_unaided_distance = unaided_distance_obj
            exam.visual_accuity_pinhole_aided_distance = pinhole_aided_distance_obj
            exam.visual_accuity_pinhole_unaided_distance = pinhole_unaided_distance_obj

            prescription_temp = form3.save(commit=False)
            prescription_temp.prescriber = request.user.ophthalmologistusermodel
            prescription_temp.save()
            exam.occular_exam_information = form2.save()
            exam.prescription = prescription_temp
            exam.status = ExamModel.status_choices["postexam"]
            exam.save()
            # treatment.save()
            prescription_temp.os_visual_acuity_distance = (
                exam.visual_accuity_aided_string_left_distance
            )
            prescription_temp.od_visual_acuity_distance = (
                exam.visual_accuity_aided_string_right_distance
            )
            prescription_temp.os_visual_acuity_near = (
                exam.visual_accuity_aided_string_left_near
            )
            prescription_temp.od_visual_acuity_near = (
                exam.visual_accuity_aided_string_right_near
            )
            prescription_temp.save()
            return redirect(reverse("exam_details", kwargs={"exam_id": exam_id}))

        for field, errors in aided_near.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}", extra_tags=f"{field}")
        for field, error in unaided_near.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")
        for field, error in pinhole_aided_near.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")
        for field, error in pinhole_unaided_near.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")
        for field, error in aided_distance.errors:
            for error in errors:
                messages.error(request, f"{field}: {error}")
        for field, error in unaided_distance.errors:
            for error in errors:
                messages.error(request, f"{field}: {error}")
        for field, error in pinhole_aided_distance.errors:
            for error in errors:
                messages.error(request, f"{field}: {error}")
        for field, error in pinhole_unaided_distance.errors:
            for error in errors:
                messages.error(request, f"{field}: {error}")
        for field, errors in occular_form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}", extra_tags=f"{field}")
        for field, errors in prescription_form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}", extra_tags=f"{field}")

        return render(
            request,
            "exam_data_submission.html",
            {
                "form": form,
                "treatment": treatment,
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


def _validate_accuity(request, parent, child, distance_aid):
    if child.visual_acuity_measure_left and not parent.visual_acuity_measure_left:
        messages.add_message(
            request,
            messages.ERROR,
            "Left eye values do not match",
            extra_tags=f"{distance_aid}_left",
        )
    if child.visual_acuity_measure_right and not parent.visual_acuity_measure_right:
        messages.add_message(
            request,
            messages.ERROR,
            "Right eye values do not match",
            extra_tags=f"{distance_aid}_right",
        )
    if child.visual_acuity_measure_both and not parent.visual_acuity_measure_both:
        messages.add_message(
            request,
            messages.ERROR,
            "Both eye values do not match",
            extra_tags=f"{distance_aid}_both",
        )
