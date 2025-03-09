from django import forms

from ophthalmology_portal.Core.models import (
    ManagerUserModel,
    OphthalmologistUserModel,
    PatientUserModel,
)


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


class ManagerUserForm(forms.ModelForm):
    class Meta:
        model = ManagerUserModel
        fields = ["first_name", "last_name", "email"]


class OphthalmologistUserForm(forms.ModelForm):
    class Meta:
        model = OphthalmologistUserModel
        fields = ["first_name", "last_name", "email", "gender"]
