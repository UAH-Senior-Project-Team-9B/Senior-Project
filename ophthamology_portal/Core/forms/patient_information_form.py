from Core.models import PatientUser
from django import forms


class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientUser
        fields = [
            "patient_id",
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
