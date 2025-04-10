from django import forms

from ophthalmology_portal.Core.models import PrescriptionModel


class PrescriptionCreationForm(forms.ModelForm):
    class Meta:
        model = PrescriptionModel
        fields = "__all__"
        exclude = ["prescriber", "patient", "os_visual_acuity_distance", "os_visual_acuity_near", "od_visual_acuity_distance", "od_visual_acuity_near"]


class PrescriptionViewForm(forms.ModelForm):
    class Meta:
        model = PrescriptionModel
        fields = "__all__"
        exclude = ["prescriber", "patient"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
