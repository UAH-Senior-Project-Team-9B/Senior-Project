from django.db import models


class PatientInformation(models.Model):
    patient_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(
        max_length=5,
        choices=[
            ("Dr.", "Dr."),
            ("Mr.", "Mr."),
            ("Mrs.", "Mrs."),
            ("Ms.", "Ms."),
        ],
    )
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
    )
    date_of_birth = models.DateField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=100)
    social_security_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.patient_id}"
