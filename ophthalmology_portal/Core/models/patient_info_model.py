from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

from ophthalmology_portal.Core.models import user_models

class EmergencyContactModel(models.Model):
    patient = models.OneToOneField(
        user_models.PatientUserModel, on_delete=models.CASCADE
    )
    contact_title = models.CharField(
        max_length=5,
        choices=[("Dr.", "Dr."), ("Mr.", "Mr."), ("Mrs.", "Mrs."), ("Ms.", "Ms.")],
    )
    contact_first_name = models.CharField(max_length=30)
    contact_middle_initial = models.CharField(max_length=1, blank=True)
    contact_last_name = models.CharField(max_length=30)
    contact_relationship = models.CharField(max_length=30)
    contact_phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r"^(?:[(][0-9]{3}[)][. -]|[(][0-9]{3}[)]|[0-9]{3}[. -])[0-9]{3}[ .-][0-9]{4}$",
                message="Phone number must follow regulations",
            )
        ],
    )
    contact_email = models.EmailField()


class InsuranceProviderModel(models.Model):
    patient = models.OneToOneField(
        user_models.PatientUserModel, on_delete=models.CASCADE
    )
    insurance_provider = models.CharField(max_length=50)
    contract_number = models.CharField(max_length=13)  # NOT A PHONE NUMBER
    group_number = models.CharField(max_length=9)
    effective_date = models.DateField()
    co_pay = models.DecimalField(decimal_places=2, max_digits=255, validators=[MinValueValidator(0)])
    insurance_street_address = models.CharField(max_length=100)
    insurance_city = models.CharField(max_length=50)
    insurance_state = models.CharField(max_length=15, choices=user_models.state_choices)
    insurance_zip_code = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r"^\d{5}-\d{4}$|^\d{5}$",
                message="Zipcode must be in the format XXXXX or XXXXX-XXXX",
            )
        ],
    )
    insurance_phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r"^(?:[(][0-9]{3}[)][. -]|[(][0-9]{3}[)]|[0-9]{3}[. -])[0-9]{3}[ .-][0-9]{4}$",
                message="Phone number must follow regulations",
            )
        ],
    )
    primary_care_provider = models.CharField(max_length=255)
