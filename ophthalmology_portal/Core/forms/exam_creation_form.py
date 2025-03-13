from django import forms

from ophthalmology_portal.Core.models import ExamModel


class ExamCreationPostForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"

class ExamCreationMainForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = ["patient"]
        exclude = ["date", "time"]
