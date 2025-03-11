from django import forms

from ophthalmology_portal.Core.models import PrescriptionModel


class PrescriptionCreationForm(forms.ModelForm):
    class Meta:
        model = PrescriptionModel
        fields = "__all__"
