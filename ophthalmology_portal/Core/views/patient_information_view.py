import datetime
from zoneinfo import ZoneInfo

from django.contrib import messages
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import (
    EmergencyContactForm,
    InsuranceProviderForm,
    PatientUserUpdateForm,
    PatientUserViewForm,
)
from ophthalmology_portal.Core.forms.patient_info_form import (
    EmergencyContactViewOnlyForm,
    InsuranceProviderViewOnlyForm,
    TreatmentForm,
)
from ophthalmology_portal.Core.forms.user_forms import PatientUserViewOnlyForm
from ophthalmology_portal.Core.models import ExamModel, PatientUserModel
from ophthalmology_portal.Core.models.patient_info_model import (
    EmergencyContactModel,
    InsuranceProviderModel,
)
from ophthalmology_portal.Core.views.base_view import BaseView


class PatientInformationView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not self.patient_verification(request.user):
            raise Http404

        patient = PatientUserModel.objects.get(user=request.user)
        patient_information_form = PatientUserViewForm(instance=patient)
        emergency_contact_form = EmergencyContactForm(
            instance=patient.emergencycontactmodel
        )
        insurance_provider_form = InsuranceProviderForm(
            instance=patient.insuranceprovidermodel
        )
        try:
            treatment = TreatmentForm(instance=patient.treatmentsmodel)
        except:
            treatment = TreatmentForm()

        return render(
            request,
            "patient_information_template.html",
            {
                "patient_id": patient.id,
                "patient_information_form": patient_information_form,
                "base_template_name": self.get_base_template(request.user),
                "emergency_contact_form": emergency_contact_form,
                "insurance_provider_form": insurance_provider_form,
                "treatment": treatment,
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = PatientUserUpdateForm(request.POST)
        form2 = EmergencyContactForm(request.POST)
        form3 = InsuranceProviderForm(request.POST)

        if form.is_valid() and form2.is_valid() and form3.is_valid():
            patient = PatientUserModel.objects.get(user=request.user)
            emergency = EmergencyContactModel.objects.get(patient=patient)
            insurance = InsuranceProviderModel.objects.get(patient=patient)
            form = PatientUserUpdateForm(request.POST, instance=patient)
            form2 = EmergencyContactForm(request.POST, instance=emergency)
            form3 = InsuranceProviderForm(request.POST, instance=insurance)

            form.save()
            form2.save()
            form3.save()
            return redirect(reverse("patient_information"))
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{error}", extra_tags=f"{field}")
        for field, errors in form2.errors.items():
            for error in errors:
                messages.error(request, f"{error}", extra_tags=f"{field}")
        for field, errors in form3.errors.items():
            for error in errors:
                messages.error(request, f"{error}", extra_tags=f"{field}")
        return redirect(reverse("patient_information"))


class PatientInformationOtherView(BaseView):
    def get(self, request: HttpRequest, patient, *args, **kwargs):
        if not self.manager_verification(request.user) and not self.doctor_verification(
            request.user
        ):
            raise Http404
        patient = PatientUserModel.objects.get(id=patient)
        patient_information = PatientUserViewOnlyForm(instance=patient)
        emergency_contact = EmergencyContactViewOnlyForm(
            instance=patient.emergencycontactmodel
        )
        insurance_provider = InsuranceProviderViewOnlyForm(
            instance=patient.insuranceprovidermodel
        )
        try:
            treatment = TreatmentForm(instance=patient.treatmentsmodel)
        except:
            treatment = TreatmentForm()

        if request.path == f"/patient-list/{patient.id}/":
            exam_url = "patient_history_exam"
            exam_button = "View Patient Exam History"
            exam_button_id = patient.id
        else:
            exam_url = "daily_exam_instance"
            exam_button = "View Current Exam"

            exam_button_id = ExamModel.objects.get(
                patient=patient,
                date=datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date(),
            ).id
        return render(
            request,
            "patient_information_template_view_only.html",
            {
                "exam_button": exam_button,
                "exam_url": exam_url,
                "exam_button_id": exam_button_id,
                "patient_information": patient_information,
                "patient_id": patient.id,
                "base_template_name": self.get_base_template(request.user),
                "emergency_contact": emergency_contact,
                "insurance_provider": insurance_provider,
                "treatment": treatment,
            },
        )
