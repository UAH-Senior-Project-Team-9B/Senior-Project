from django import forms

from ophthalmology_portal.Core.models import ExamModel


class ExamCreationForm(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={'type': 'date'})
        }
