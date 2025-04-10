from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from ophthalmology_portal.Core.forms import (
    PatientUserForm,
    EmergencyContactForm,
    InsuranceProviderForm,
    PatientUserUpdateForm
)
from ophthalmology_portal.Core.models import PatientUserModel
from ophthalmology_portal.Core.views.base_view import BaseView


class PatientInformationView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        patient = PatientUserModel.objects.get(user=request.user)
        patient_information_form = PatientUserForm(instance=patient)
        emergency_contact_form = EmergencyContactForm(
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
