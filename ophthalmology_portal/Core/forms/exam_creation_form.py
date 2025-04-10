from django import forms

from ophthalmology_portal.Core.models import ExamModel


class ExamCreationPostForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["status"]


class ExamCreationMainForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = ["patient"]
        exclude = ["date", "time"]


class ExamViewForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["prescription", "occular_exam_information", "visual_accuity_unaided_near", "visual_accuity_aided_near", "visual_accuity_pinhole_unaided_near", "visual_accuity_pinhole_aided_near", "visual_accuity_unaided_distance", "visual_accuity_aided_distance", "visual_accuity_pinhole_unaided_distance", "visual_accuity_pinhole_aided_distance"]
        widgets = {
            'status': forms.TextInput
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

class ExamPatientViewNonCompleteForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["prescription", "occular_exam_information", "visual_accuity_unaided_near", "visual_accuity_aided_near", "visual_accuity_pinhole_unaided_near", "visual_accuity_pinhole_aided_near", "visual_accuity_unaided_distance", "visual_accuity_aided_distance", "visual_accuity_pinhole_unaided_distance", "visual_accuity_pinhole_aided_distance", "visual_accuity_unaided_string_right_near", "visual_accuity_unaided_string_left_near", "visual_accuity_unaided_string_both_near", "visual_accuity_aided_string_right_near", "visual_accuity_aided_string_left_near", "visual_accuity_aided_string_both_near", "visual_accuity_unaided_string_right_distance", "visual_accuity_unaided_string_left_distance", "visual_accuity_unaided_string_both_distance", "visual_accuity_aided_string_right_distance", "visual_accuity_aided_string_left_distance", "visual_accuity_aided_string_both_distance"]
        widgets = {
            'status': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

class ExamDoctorViewForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["prescription", "occular_exam_information", "visual_accuity_unaided_near", "visual_accuity_aided_near", "visual_accuity_pinhole_unaided_near", "visual_accuity_pinhole_aided_near", "visual_accuity_unaided_distance", "visual_accuity_aided_distance", "visual_accuity_pinhole_unaided_distance", "visual_accuity_pinhole_aided_distance", "visual_accuity_unaided_string_right_near", "visual_accuity_unaided_string_left_near", "visual_accuity_unaided_string_both_near", "visual_accuity_aided_string_right_near", "visual_accuity_aided_string_left_near", "visual_accuity_aided_string_both_near", "visual_accuity_unaided_string_right_distance", "visual_accuity_unaided_string_left_distance", "visual_accuity_unaided_string_both_distance", "visual_accuity_aided_string_right_distance", "visual_accuity_aided_string_left_distance", "visual_accuity_aided_string_both_distance"]
        widgets = {
            'status': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True


class ExamManagerViewForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["visual_accuity_information", "occular_exam_information"]
        widgets = {
            'status': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

class ExamManagerArrivalTimeForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["visual_accuity_information", "occular_exam_information"]
        widgets = {
            'status': forms.TextInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'arrival_time':
                pass
            else:
                self.fields[field].disabled = True

class ExamTimeForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = ["date", "time"]

class ExamArrivalForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = ["arrival_time"]
