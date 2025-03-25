from bdb import effective
from django.db import models

from ophthalmology_portal.Core.models import user_models

class EmergencyContactModel(models.Model):
    patient = models.ForeignKey(user_models.PatientUserModel, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=5,
        choices=[
            ("Dr.", "Dr."),
            ("Mr.", "Mr."),
            ("Mrs.", "Mrs."),
            ("Ms.", "Ms.")
        ]
    )
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=30)
    relationship = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class InsureanceProvider:
    patient = models.ForeignKey(user_models.PatientUserModel, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    contract_number = models.CharField(max_length=13) # NOT A PHONE NUMBER
    group_number = models.IntegerField(max_length=4)
    effective_date = models.DateField()
    co_pay = models.FloatField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(
        max_length=15,
        choices=user_models.state_choices
    )
    zip_code = models.IntegerField(max_length=10)
    phone_number = models.IntegerField(max_length=10)
