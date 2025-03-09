from django import forms

from ophthalmology_portal.Core.models import AppointmentRequest


class AppointmentRequestForm(forms.ModelForm):
    appointment_time = forms.TimeField(
        widget=forms.Select(
            choices=[
                ("09:00", "09:00 AM"),
                ("10:00", "10:00 AM"),
                ("11:00", "11:00 AM"),
                ("12:00", "12:00 PM"),
                ("13:00", "01:00 PM"),
                ("14:00", "02:00 PM"),
                ("15:00", "03:00 PM"),
                ("16:00", "04:00 PM"),
                ("17:00", "05:00 PM"),
            ]
        )
    )

    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    class Meta:
        model = AppointmentRequest
        fields = [
            "first_name",
            "middle_initial",
            "last_name",
            "date_of_birth",
            "appointment_date",
            "appointment_time",
            "request_details",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "middle_initial": forms.TextInput(
                attrs={"class": "form-control", "maxlength": 1}
            ),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "request_details": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
        }
