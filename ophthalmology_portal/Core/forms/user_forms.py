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
            "social_security_number",
            "email",
        ]
        widgets = {
            "phone_number": forms.TextInput(attrs={
                "id": "phone_number",  # Needed for JavaScript selector
                "placeholder": "(123) 456-7890"
            }),
        }



class PatientUserViewForm(forms.ModelForm):
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
            "social_security_number",
            "email",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["social_security_number"].disabled = True


class PatientUserViewOnlyForm(forms.ModelForm):
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
            "social_security_number",
            "email",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

class PatientUserUpdateForm(forms.ModelForm):
    class Meta:
        model = PatientUserModel
        fields = [
            "title",
            "first_name",
            "middle_initial",
            "last_name",
            "gender",
            "street_address",
            "city",
            "state",
            "zip_code",
            "phone_number",
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
