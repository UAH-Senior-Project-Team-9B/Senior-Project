from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ophthalmology_portal.Core.models import user_models

visual_acuity_choices = {
    "20/10": "20/10",
    "20/12.5": "20/12.5",
    "20/16": "20/16",
    "20/20": "20/20",
    "20/25": "20/25",
    "20/32": "20/32",
    "20/40": "20/40",
    "20/50": "20/50",
    "20/63": "20/63",
    "20/80": "20/80",
    "20/100": "20/100",
    "20/125": "20/125",
    "20/160": "20/160",
    "20/200": "20/200",
}


class PrescriptionModel(models.Model):
    prescriber = models.ForeignKey(
        user_models.OphthalmologistUserModel, on_delete=models.CASCADE
    )
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
    os_visual_acuity_distance = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    os_visual_acuity_near = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    od_visual_acuity_distance = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    od_visual_acuity_near = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
