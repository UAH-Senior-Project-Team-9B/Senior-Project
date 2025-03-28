import sys

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ophthalmology_portal.Core"

    def ready(self):
        if "runserver" in sys.argv:
            from django.contrib.auth.models import (
                Group,  # Prevents circular import
                Permission,
            )

            patient = Group.objects.get_or_create(name="Patients")
            manager = Group.objects.get_or_create(name="Office Manager")
            doctor = Group.objects.get_or_create(name="Ophthalmologist")
            if patient[1]:
                for permission in Permission.objects.filter(name="Patient Permissions"):
                    patient[0].permissions.add(permission)
            if manager[1]:
                for permission in Permission.objects.filter(name="Manager Permissions"):
                    manager[0].permissions.add(permission)
            if doctor[1]:
                for permission in Permission.objects.filter(name="Doctor Permissions"):
                    doctor[0].permissions.add(permission)
