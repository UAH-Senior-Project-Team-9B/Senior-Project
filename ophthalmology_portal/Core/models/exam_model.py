import datetime
from zoneinfo import ZoneInfo

from django.db import models

from ophthalmology_portal.Core.models import user_models
from ophthalmology_portal.Core.models.prescription_model import PrescriptionModel
from ophthalmology_portal.Core.models.test_information_model import (
    OccularExamModel,
    VisualAccuityModel,
)


class ExamModel(models.Model):
    completed = models.BooleanField(default=False)

    status_choices = {
        "pending": "Pending",
        "upcoming": "Upcoming",
        "waiting": "In Wait Room",
        "progressing": "Exam In Progress",
        "complete": "Completed",
    }
    status = models.CharField(
        max_length=16,
        choices=status_choices,
        null=True,
        blank=True,
    )
    date = models.DateField()
    time = models.TimeField()
    arrival_time = models.TimeField(blank=True, null=True)
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
    visual_accuity_unaided_near = models.OneToOneField(
        VisualAccuityModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="exam_unaided_near",
    )
    visual_accuity_aided_near = models.OneToOneField(
        VisualAccuityModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="exam_aided_near",
    )
    visual_accuity_pinhole_unaided_near = models.OneToOneField(
        VisualAccuityModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="exam_unaided_ph_near",
    )
    visual_accuity_pinhole_aided_near = models.OneToOneField(
        VisualAccuityModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="exam_aided_ph_near",
    )

    visual_accuity_unaided_distance = models.OneToOneField(
        VisualAccuityModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="exam_unaided_distance",
    )
    visual_accuity_aided_distance = models.OneToOneField(
        VisualAccuityModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="exam_aided_distance",
    )
    visual_accuity_pinhole_unaided_distance = models.OneToOneField(
        VisualAccuityModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="exam_unaided_ph_distance",
    )
    visual_accuity_pinhole_aided_distance = models.OneToOneField(
        VisualAccuityModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="exam_aided_ph_distance",
    )
    visual_accuity_unaided_string_right_near = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_unaided_string_left_near = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_unaided_string_both_near = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_aided_string_right_near = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_aided_string_left_near = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_aided_string_both_near = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )

    visual_accuity_unaided_string_right_distance = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_unaided_string_left_distance = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_unaided_string_both_distance = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_aided_string_right_distance = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_aided_string_left_distance = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )
    visual_accuity_aided_string_both_distance = models.CharField(
        max_length=255, null=True, blank=True, default="Not Recorded"
    )

    reason_for_visit = models.TextField(max_length=255)

    def unaided_string_near(self):
        accuity = self.visual_accuity_unaided_near
        pinhole = self.visual_accuity_pinhole_unaided_near
        if accuity.visual_acuity_measure_right and pinhole.visual_acuity_measure_right:
            self.visual_accuity_unaided_string_right_near = f"NscOD {accuity.visual_acuity_measure_right} PH {pinhole.visual_acuity_measure_right}"
        elif accuity.visual_acuity_measure_right:
            self.visual_accuity_unaided_string_right_near = (
                f"NscOD {accuity.visual_acuity_measure_right}"
            )
        if accuity.visual_acuity_measure_left and pinhole.visual_acuity_measure_left:
            self.visual_accuity_unaided_string_left_near = f"NscOS {accuity.visual_acuity_measure_left} PH {pinhole.visual_acuity_measure_left}"
        elif accuity.visual_acuity_measure_left:
            self.visual_accuity_unaided_string_left_near = (
                f"NscOS {accuity.visual_acuity_measure_left}"
            )
        if accuity.visual_acuity_measure_both and pinhole.visual_acuity_measure_both:
            self.visual_accuity_unaided_string_both_near = f"NscOU {accuity.visual_acuity_measure_both} PH {pinhole.visual_acuity_measure_both}"
        elif accuity.visual_acuity_measure_both:
            self.visual_accuity_unaided_string_both_near = (
                f"NscOU {accuity.visual_acuity_measure_both}"
            )

    def aided_string_near(self):
        accuity = self.visual_accuity_aided_near
        pinhole = self.visual_accuity_pinhole_aided_near
        if accuity.visual_acuity_measure_right and pinhole.visual_acuity_measure_right:
            self.visual_accuity_aided_string_right_near = f"NccOD {accuity.visual_acuity_measure_right} PH {pinhole.visual_acuity_measure_right}"
        elif accuity.visual_acuity_measure_right:
            self.visual_accuity_aided_string_right_near = (
                f"NscOD {accuity.visual_acuity_measure_right}"
            )
        if accuity.visual_acuity_measure_left and pinhole.visual_acuity_measure_left:
            self.visual_accuity_aided_string_left_near = f"NccOS {accuity.visual_acuity_measure_left} PH {pinhole.visual_acuity_measure_left}"
        elif accuity.visual_acuity_measure_left:
            self.visual_accuity_aided_string_left_near = (
                f"NscOS {accuity.visual_acuity_measure_left}"
            )
        if accuity.visual_acuity_measure_both and pinhole.visual_acuity_measure_both:
            self.visual_accuity_aided_string_both_near = f"NccOU {accuity.visual_acuity_measure_both} PH {pinhole.visual_acuity_measure_both}"
        elif accuity.visual_acuity_measure_both:
            self.visual_accuity_aided_string_both_near = (
                f"NscOU {accuity.visual_acuity_measure_both}"
            )

    def unaided_string_distance(self):
        accuity = self.visual_accuity_unaided_distance
        pinhole = self.visual_accuity_pinhole_unaided_distance
        if accuity.visual_acuity_measure_right and pinhole.visual_acuity_measure_right:
            self.visual_accuity_unaided_string_right_distance = f"DscOD {accuity.visual_acuity_measure_right} PH {pinhole.visual_acuity_measure_right}"
        elif accuity.visual_acuity_measure_right:
            self.visual_accuity_unaided_string_right_distance = (
                f"DscOD {accuity.visual_acuity_measure_right}"
            )
        if accuity.visual_acuity_measure_left and pinhole.visual_acuity_measure_left:
            self.visual_accuity_unaided_string_left_distance = f"DscOS {accuity.visual_acuity_measure_left} PH {pinhole.visual_acuity_measure_left}"
        elif accuity.visual_acuity_measure_left:
            self.visual_accuity_unaided_string_left_distance = (
                f"DscOS {accuity.visual_acuity_measure_left}"
            )
        if accuity.visual_acuity_measure_both and pinhole.visual_acuity_measure_both:
            self.visual_accuity_unaided_string_both_distance = f"DscOU {accuity.visual_acuity_measure_both} PH {pinhole.visual_acuity_measure_both}"
        elif accuity.visual_acuity_measure_both:
            self.visual_accuity_unaided_string_both_distance = (
                f"DscOU {accuity.visual_acuity_measure_both}"
            )

    def aided_string_distance(self):
        accuity = self.visual_accuity_aided_distance
        pinhole = self.visual_accuity_pinhole_aided_distance
        if accuity.visual_acuity_measure_right and pinhole.visual_acuity_measure_right:
            self.visual_accuity_aided_string_right_distance = f"DccOD {accuity.visual_acuity_measure_right} PH {pinhole.visual_acuity_measure_right}"
        elif accuity.visual_acuity_measure_right:
            self.visual_accuity_aided_string_right_distance = (
                f"DscOD {accuity.visual_acuity_measure_right}"
            )
        if accuity.visual_acuity_measure_left and pinhole.visual_acuity_measure_left:
            self.visual_accuity_aided_string_left_distance = f"DccOS {accuity.visual_acuity_measure_left} PH {pinhole.visual_acuity_measure_left}"
        elif accuity.visual_acuity_measure_left:
            self.visual_accuity_aided_string_left_distance = (
                f"DscOS {accuity.visual_acuity_measure_left}"
            )
        if accuity.visual_acuity_measure_both and pinhole.visual_acuity_measure_both:
            self.visual_accuity_aided_string_both_distance = f"DccOU {accuity.visual_acuity_measure_both} PH {pinhole.visual_acuity_measure_both}"
        elif accuity.visual_acuity_measure_both:
            self.visual_accuity_aided_string_both_distance = (
                f"DscOU {accuity.visual_acuity_measure_both}"
            )

    def save(self, **kwargs):
        if not self.status:
            self.status = "Upcoming"
        if self.visual_accuity_aided_near:
            self.aided_string_near()
        if self.visual_accuity_unaided_near:
            self.unaided_string_near()
        if self.visual_accuity_aided_distance:
            self.aided_string_distance()
        if self.visual_accuity_unaided_distance:
            self.unaided_string_distance()
        super().save()

    class Meta:
        ordering = ["-date", "-time"]
        permissions = [
            ("patient", "Patient Permissions"),
            ("doctor", "Doctor Permissions"),
            ("manager", "Manager Permissions"),
        ]
        unique_together = ["date", "time", "doctor"]

    def __str__(self):
        return f"Exam on {self.date} at {self.time}"

    def in_lobby(self):
        self.status = "In Wait Room"
        self.arrival_time = datetime.datetime.now(
            ZoneInfo("America/Indiana/Knox")
        ).time()
        self.save()

    def in_progress(self):
        self.status = "Exam In Progress"
        self.save()

    def complete(self):
        if self.occular_exam_information:
            self.status = "Completed"
            self.save()
            return True
        else:
            return False

    def stageable(self):
        if self.date == datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date():
            if self.status != "Completed" and self.status != "Pending":
                return True
        else:
            return False
