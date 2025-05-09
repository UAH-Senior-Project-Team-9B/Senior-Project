from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

state_choices = {
    "Alabama": "Alabama",
    "Alaska": "Alaska",
    "Arizona": "Arisona",
    "Arkansas": "Arkansas",
    "California": "California",
    "Colorado": "Colorado",
    "Connecticut": "Connecticut",
    "Delaware": "Delaware",
    "Florida": "Florida",
    "Georgia": "Georgia",
    "Hawaii": "Hawaii",
    "Idaho": "Idaho",
    "Illinois": "Illinois",
    "Indiana": "Indiana",
    "Iowa": "Iowa",
    "Kansas": "Kansas",
    "Kentucky": "Kentucky",
    "Louisiana": "Louisiana",
    "Maine": "Maine",
    "Maryland": "Maryland",
    "Massachusetts": "Massachusetts",
    "Michigan": "Michigan",
    "Minnesota": "Minnesota",
    "Mississippi": "Mississippi",
    "Missouri": "Missouri",
    "Montana": "Montana",
    "Nebraska": "Nebraska",
    "Nevada": "Nevada",
    "New Hampshire": "New Hampsire",
    "New Jersey": "New Jersey",
    "New Mexico": "New Mexico",
    "New York": "New York",
    "North Carolina": "North Carolina",
    "North Dakota": "North Dakota",
    "Ohio": "Ohio",
    "Oklahoma": "Oklahoma",
    "Oregon": "Oregon",
    "Pennsylvania": "Pennsylvania",
    "Rhode Island": "Rhode Island",
    "South Carolina": "South Carolina",
    "South Dakota": "South Dakota",
    "Tennessee": "Tennessee",
    "Texas": "Texas",
    "Utah": "Utah",
    "Vermont": "Vermont",
    "Virginia": "Virginia",
    "Washington": "Washington",
    "West Virginia": "West Virginia",
    "Wisconsin": "Wisconsin",
    "Wyoming": "Wyoming",
    "Other": "Other",
}


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
    state = models.CharField(max_length=20, choices=state_choices)
    zip_code = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{5}-\d{4}$|^\d{5}$",
                message="Zipcode must be in the format XXXXX or XXXXX-XXXX",
            )
        ],
    )
    phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r"^(?:[(][0-9]{3}[)][. -]|[(][0-9]{3}[)]|[0-9]{3}[. -])[0-9]{3}[ .-][0-9]{4}$",
                message="Phone number must follow regulations",
            )
        ],
    )
    social_security_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{3}-\d{2}-\d{4}$",
                message="SSN must be in the format XXX-XX-XXXX",
            )
        ],
    )
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
