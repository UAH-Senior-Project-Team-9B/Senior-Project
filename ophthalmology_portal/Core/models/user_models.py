from django.contrib.auth.models import User
from django.db import models


class PatientUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
        return f"{self.first_name} {self.last_name}"


class ManagerUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class OphthalmologistUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
