from django import forms
from django.core.exceptions import ValidationError
from ophthalmology_portal.Core.models import OccularExamModel, VisualAccuityModel


class VisualAccuityCreationForm(forms.ModelForm):
    class Meta:
        model = VisualAccuityModel
        fields = "__all__"


class OccularExamCreationForm(forms.ModelForm):
    class Meta:
        model = OccularExamModel
        fields = "__all__"
    def cleaned_data(self):
        if self.fields['other']:
            if not self.fields['other_information']:
                raise ValidationError("If other is selected, the other information field must be filled in.", code="other_information")


class VisualAccuityViewForm(forms.ModelForm):
    class Meta:
        model = VisualAccuityModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True


class OccularExamViewForm(forms.ModelForm):
    class Meta:
        model = OccularExamModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
