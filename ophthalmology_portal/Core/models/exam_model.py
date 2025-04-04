from django.db import models

from ophthalmology_portal.Core.models import user_models
from ophthalmology_portal.Core.models.prescription_model import PrescriptionModel
from ophthalmology_portal.Core.models.test_information_model import (
    OccularExamModel,
    VisualAccuityModel,
)


class ExamModel(models.Model):
    status = models.CharField(
        max_length=12,
        choices={
            "Pending": "Pending",
            "Upcoming": "Upcoming",
            "In Wait Room": "In Wait Room",
            "In Progress": "In Progress",
            "Completed": "Completed",
            "Canceled": "Canceled",
        },
        null=True,
        blank=True,
    )
    date = models.DateField()
    time = models.TimeField()
    patient = models.ForeignKey(user_models.PatientUserModel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        user_models.OphthalmologistUserModel, on_delete=models.CASCADE
    )
    prescription = models.OneToOneField(
        PrescriptionModel, on_delete=models.CASCADE, blank=True, null=True
    )
    occular_exam_information = models.OneToOneField(
        OccularExamModel, on_delete=models.CASCADE, blank=True, null=True
    )
    visual_accuity_information = models.OneToOneField(
        VisualAccuityModel, on_delete=models.CASCADE, blank=True, null=True
    )
    reason_for_visit = models.TextField(max_length=255)

    def save(self, **kwargs):
        if not self.status:
            self.status = "pending"
        if self.occular_exam_information and self.visual_accuity_information:
            self.status = "completed"
        super().save()

    class Meta:
        ordering = ["-date", "-time"]
        permissions = [
            ("patient", "Patient Permissions"),
            ("doctor", "Doctor Permissions"),
            ("manager", "Manager Permissions"),
        ]
        unique_together = ["date", "time"]

    def __str__(self):
        return f"Exam on {self.date} at {self.time}"

    def in_lobby(self):
        self.status = "In Wait Room"
        self.save()

    def in_progress(self):
        self.status = "In Progress"
        self.save()

    def complete(self):
        self.status = "Completed"
        self.save()

    def cancel(self):
        self.status = "Canceled"
        self.save()
