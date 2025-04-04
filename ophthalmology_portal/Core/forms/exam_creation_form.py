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


class ExamPatientViewForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["visual_accuity_information", "occular_exam_information"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True


class ExamDoctorViewForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["visual_accuity_information", "occular_exam_information"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True


class ExamManagerViewForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        exclude = ["visual_accuity_information", "occular_exam_information"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
