from django import forms

from ophthalmology_portal.Core.models import InsuranceClaimModel


class InsuranceClaimForm(forms.ModelForm):
    class Meta:
        model = InsuranceClaimModel
        fields = "__all__"
        exclude = ["exam"]
