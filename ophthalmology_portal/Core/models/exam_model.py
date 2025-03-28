from django.db import models

from ophthalmology_portal.Core.models import user_models
from ophthalmology_portal.Core.models.prescription_model import PrescriptionModel
from ophthalmology_portal.Core.models.test_information_model import (
    OccularExamModel,
    VisualAccuityModel,
)


class ExamModel(models.Model):
    status = models.CharField(
        max_length=11,
        choices={
            "pending": "Pending",
            "upcoming": "Upcoming",
            "waiting": "In Wait Room",
            "progressing": "In Progress",
            "completed": "Completed",
            "canceled": "Canceled",
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
            self.status = "upcoming"
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

    def __str__(self):
        return f"Exam on {self.date} at {self.time}"

    def in_lobby(self):
        self.status = "waiting"
        self.save()

    def in_progress(self):
        self.status = "progressing"
        self.save()

    def complete(self):
        self.status = "complete"
        self.save()

    def cancel(self):
        self.status = "canceled"
        self.save()
