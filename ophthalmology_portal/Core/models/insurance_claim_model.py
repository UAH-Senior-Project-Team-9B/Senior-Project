from django.db import models

from ophthalmology_portal.Core.models import exam_model


class InsuranceClaimModel(models.Model):
    exam = models.ForeignKey(exam_model.ExamModel, on_delete=models.CASCADE)
    treatment_details = models.TextField(
        max_length=65535,
        null=True,
        blank=True,
        default=None,
    )
    cost_breakdown = models.TextField(
        max_length=65535,
        null=True,
        blank=True,
        default=None,
    )
