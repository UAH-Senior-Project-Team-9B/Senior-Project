from django import forms

from ophthalmology_portal.Core.models import (
    EmergencyContactModel,
    InsuranceProviderModel,
)
from ophthalmology_portal.Core.models.patient_info_model import TreatmentsModel


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContactModel
        fields = "__all__"
        exclude = ["patient"]
        labels = {
            "contact_title": "Title",
            "contact_first_name": "First Name",
            "contact_middle_initial": "Middle Initial",
            "contact_last_name": "Last Name",
            "contact_relationship": "Relationship",
            "contact_phone_number": "Phone Number",
            "contact_email": "Email",
        }
        widgets = {
            "contact_phone_number": forms.TextInput(
                attrs={
                    "id": "contact_phone_number",
                    "placeholder": "(123) 456-7890",
                    "oninput": "this.value=this.value.replace(/[^0-9]/g,'').replace(/(\\d{3})(\\d{3})(\\d{0,4})/,'($1) $2-$3');",
                }
            )
        }


class EmergencyContactViewOnlyForm(forms.ModelForm):
    class Meta:
        model = EmergencyContactModel
        fields = "__all__"
        exclude = ["patient"]
        labels = {
            "contact_title": "Title",
            "contact_first_name": "First Name",
            "contact_middle_initial": "Middle Initial",
            "contact_last_name": "Last Name",
            "contact_relationship": "Relationship",
            "contact_phone_number": "Phone Number",
            "contact_email": "Email",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True


class InsuranceProviderForm(forms.ModelForm):
    class Meta:
        model = InsuranceProviderModel
        fields = "__all__"
        exclude = ["patient"]
        labels = {
            "insurance_street_address": "Street Address",
            "insurance_city": "City",
            "insurance_state": "State",
            "insurance_zip_code": "Zip Code",
            "insurance_phone_number": "Phone Number",
        }
        widgets = {
            "insurance_phone_number": forms.TextInput(
                attrs={
                    "id": "insurance_phone_number",
                    "placeholder": "(123) 456-7890",
                    "oninput": "this.value=this.value.replace(/[^0-9]/g,'').replace(/(\\d{3})(\\d{3})(\\d{0,4})/,'($1) $2-$3');",
                }
            )
        }


class InsuranceProviderViewOnlyForm(forms.ModelForm):
    class Meta:
        model = InsuranceProviderModel
        fields = "__all__"
        exclude = ["patient"]
        labels = {
            "insurance_street_address": "Street Address",
            "insurance_city": "City",
            "insurance_state": "State",
            "insurance_zip_code": "Zip Code",
            "insurance_phone_number": "Phone Number",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = TreatmentsModel
        fields = "__all__"
