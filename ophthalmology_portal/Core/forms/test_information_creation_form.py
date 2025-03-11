from django import forms

from ophthalmology_portal.Core.models import OccularExamModel, VisualAccuityModel


class VisualAccuityCreationForm(forms.ModelForm):
    class Meta:
        model = VisualAccuityModel
        fields = "__all__"


class OccularExamCreationForm(forms.ModelForm):
    class Meta:
        model = OccularExamModel
        fields = "__all__"
