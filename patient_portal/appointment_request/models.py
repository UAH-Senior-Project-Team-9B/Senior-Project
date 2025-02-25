from datetime import date

from django.db import models


class AppointmentRequest(models.Model):
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    appointment_date = models.DateField(default=date.today)
    appointment_time = models.TimeField()
    request_details = models.TextField()

    class Meta:
        unique_together = [
            "appointment_date",
            "appointment_time",
        ]  # Prevent double-booking

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.appointment_date} at {self.appointment_time}"
