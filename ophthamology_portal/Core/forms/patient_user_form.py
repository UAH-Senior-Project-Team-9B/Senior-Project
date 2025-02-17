from django import forms

from ophthamology_portal.Core.models import PatientUserModel


class PatientUserForm(forms.ModelForm):
    class Meta:
        model = PatientUserModel
        fields = [
            "title",
            "first_name",
            "middle_initial",
            "last_name",
            "gender",
            "date_of_birth",
            "street_address",
            "city",
            "state",
            "zip_code",
            "phone_number",
            "emergency_contact",
            "social_security_number",
            "email",
        ]
