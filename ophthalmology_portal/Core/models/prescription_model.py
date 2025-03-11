from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ophthalmology_portal.Core.models import user_models

visual_acuity_choices = {
    10: "20/10",
    12.5: "20/12.5",
    16: "20/16",
    20: "20/20",
    25: "20/25",
    32: "20/32",
    40: "20/40",
    50: "20/50",
    63: "20/63",
    80: "20/80",
    100: "20/100",
    125: "20/125",
    160: "20/160",
    200: "20/200",
}


class PrescriptionModel(models.Model):
    prescriber = models.ForeignKey(
        user_models.OphthalmologistUserModel, on_delete=models.CASCADE
    )
    patient = models.ForeignKey(user_models.PatientUserModel, on_delete=models.CASCADE)
    date_prescribed = models.DateField(auto_now_add=True)
    od_sphere = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    od_cylinder = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    od_axis = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    od_add = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    od_prism = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    od_prism_base = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_sphere = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_cylinder = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_axis = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_add = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_prism = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_prism_base = models.DecimalField(
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    visual_acuity = models.DecimalField(
        choices=visual_acuity_choices, max_digits=4, decimal_places=1
    )
