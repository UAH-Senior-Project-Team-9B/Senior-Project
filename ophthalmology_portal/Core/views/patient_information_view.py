import datetime
from zoneinfo import ZoneInfo
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from ophthalmology_portal.Core.forms import (
    PatientUserViewForm,
    EmergencyContactForm,
    InsuranceProviderForm,
    PatientUserUpdateForm
)
from ophthalmology_portal.Core.forms.patient_info_form import EmergencyContactViewOnlyForm, InsuranceProviderViewOnlyForm
from ophthalmology_portal.Core.forms.user_forms import PatientUserViewOnlyForm
from ophthalmology_portal.Core.models import PatientUserModel, ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView


class PatientInformationView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):

        patient = PatientUserModel.objects.get(user=request.user)
        patient_information = PatientUserViewForm(instance=patient)
        emergency_contact = EmergencyContactForm(
            instance=patient.emergencycontactmodel
        )
        insurance_provider_form = InsuranceProviderForm(
            instance=patient.insuranceprovidermodel
        )
        return render(
            request,
            "patient_information_template.html",
            {
                "patient_information_form": patient_information_form,
                "base_template_name": self.get_base_template(request.user),
                "emergency_contact_form": emergency_contact_form,
                "insurance_provider_form": insurance_provider_form,
            },
        )

    def post(self, request: HttpRequest, exam_id, *args, **kwargs):
        form = PatientUserUpdateForm(request.POST)
        form2 = EmergencyContactForm(request.POST)
        form3 = InsuranceProviderForm(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
            return redirect(reverse("patient_information"))
        for field in form.errors:
            messages.error(request, form.errors[field])
        for field in form2.errors:
            messages.error(request, form2.errors[field])
        for field in form3.errors:
            messages.error(request, form3.errors[field])
        return redirect(reverse("patient_information", kwargs={"exam_id": exam_id}))


class PatientInformationOtherView(BaseView):
    def get(self, request: HttpRequest, patient, *args, **kwargs):
        patient = PatientUserModel.objects.get(id=patient)
        patient_information = PatientUserViewOnlyForm(instance=patient)
        emergency_contact = EmergencyContactViewOnlyForm(
            instance=patient.emergencycontactmodel
        )
        insurance_provider = InsuranceProviderViewOnlyForm(
            instance=patient.insuranceprovidermodel
        )
        if request.path == f"/patient-list/{patient.id}/":
            exam_url = "patient_history_exam"
            exam_button = "View Patient Exam History"
            exam_button_id = patient.id
        else:
            exam_url="daily_exam_instance"
            exam_button="View Current Exam"

            exam_button_id=ExamModel.objects.get(patient=patient, date=datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date()).id
        return render(
            request,
            "patient_information_template_view_only.html",
            {
                "exam_button": exam_button,
                "exam_url": exam_url,
                "exam_button_id": exam_button_id,
                "patient_information": patient_information,
                "base_template_name": self.get_base_template(request.user),
                "emergency_contact": emergency_contact,
                "insurance_provider": insurance_provider,
            },
        )
