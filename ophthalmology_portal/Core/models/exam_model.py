from django.db import models

from ophthalmology_portal.Core.models import user_models
from ophthalmology_portal.Core.models.prescription_model import PrescriptionModel
from ophthalmology_portal.Core.models.test_information_model import (
    OccularExamModel,
    VisualAccuityModel,
)


class ExamModel(models.Model):
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(user_models.PatientUserModel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        user_models.OphthalmologistUserModel, on_delete=models.CASCADE
    )
    prescription = models.OneToOneField(PrescriptionModel, on_delete=models.CASCADE, blank=True, null=True)
    occular_exam_information = models.OneToOneField(
        OccularExamModel, on_delete=models.CASCADE, blank=True, null=True
    )
    visual_accuity_information = models.OneToOneField(
        VisualAccuityModel, on_delete=models.CASCADE, blank=True, null=True
    )
