from django import forms
from django.core.exceptions import ValidationError

from ophthalmology_portal.Core.models import OccularExamModel, VisualAccuityModel


class BothVisualAccuityCreationForm(forms.ModelForm):
    class Meta:
        model = VisualAccuityModel
        fields = "__all__"
        exclude = [
            "corrector_indicator_right",
            "visual_acuity_measure_right",
            "pinhole_left",
            "corrector_indicator_left",
            "visual_acuity_measure_left",
        ]


class IndividualVisualAccuityCreationForm(forms.ModelForm):
    class Meta:
        model = VisualAccuityModel
        fields = "__all__"
        exclude = [
            "visual_acuity_measure_both",
            "corrector_indicator_both",
            "pinhole_both",
        ]


class OccularExamCreationForm(forms.ModelForm):
    class Meta:
        model = OccularExamModel
        fields = "__all__"

    def clean(self):
        data = self.cleaned_data
        if data["other"] and not data["other_information"]:
            raise ValidationError(
                "If other is selected, the other information field must be filled in.",
                code="other_information",
            )
        if data["other_information"] and not data["other"]:
            raise ValidationError(
                "If other is not selected, additional information is not needed.",
                code="other_information",
            )


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
