from django import forms

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


class VisualAccuitySubmissionForm(forms.ModelForm):
    class Meta:
        model = VisualAccuityModel
        fields = "__all__"


class OccularExamCreationForm(forms.ModelForm):
    class Meta:
        model = OccularExamModel
        fields = "__all__"

    def clean(self):
        data = self.cleaned_data
        if data["other"] and not data["other_information"]:
            self.add_error(
                "other",
                "If other is selected, the other information field must be filled in.",
            )
        if data["other_information"] and not data["other"]:
            self.add_error(
                "other_information",
                "If other is not selected, additional information is not needed.",
            )
        if data["custom_1"] and not data["custom_1_input"]:
            self.add_error(
                "custom_1",
                "Must define a custom field if selecting a status.",
            )
        if data["custom_1_input"] and not data["custom_1"]:
            self.add_error(
                "custom_1_input",
                "Must select a status if defining a custom field.",
            )
        if data["custom_2"] and not data["custom_2_input"]:
            self.add_error(
                "custom_2",
                "Must define a custom field if selecting a status.",
            )
        if data["custom_2_input"] and not data["custom_2"]:
            self.add_error(
                "custom_2_input",
                "Must select a status if defining a custom field.",
            )
        if data["custom_3"] and not data["custom_3_input"]:
            self.add_error(
                "custom_3",
                "Must define a custom field if selecting a status.",
            )
        if data["custom_3_input"] and not data["custom_3"]:
            self.add_error(
                "custom_3_input",
                "Must select a status if defining a custom field.",
            )
        return super().clean()


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
