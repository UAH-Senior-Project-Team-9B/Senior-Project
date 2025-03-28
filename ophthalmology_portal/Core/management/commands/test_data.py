from django.contrib.auth.models import (
    Group,
    Permission,
)
from django.core.management.base import BaseCommand

from ophthalmology_portal.Core.forms.base_user_form import BaseUserForm
from ophthalmology_portal.Core.forms.user_forms import (
    ManagerUserForm,
    OphthalmologistUserForm,
)


class Command(BaseCommand):
    help = "Generates data used for debugging. DO NOT RUN IN DEVELOPMENT."

    def handle(self, *args, **options):
        patient_group, patient_exists = Group.objects.get_or_create(name="Patients")
        manager_group, manager_exists = Group.objects.get_or_create(
            name="Office Manager"
        )
        doctor_group, doctor_exists = Group.objects.get_or_create(
            name="Ophthalmologist"
        )
        if patient_exists:
            for permission in Permission.objects.filter(name="Patient Permissions"):
                patient_group.permissions.add(permission)
        if manager_exists:
            for permission in Permission.objects.filter(name="Manager Permissions"):
                manager_group.permissions.add(permission)
        if doctor_exists:
            for permission in Permission.objects.filter(name="Doctor Permissions"):
                doctor_group.permissions.add(permission)
        user_form = BaseUserForm({"username": "manager", "password": "1234"})
        user = user_form.save(commit=False)
        user.set_password(user_form.cleaned_data["password"])
        user.save()
        form = ManagerUserForm({
            "first_name": "firstname",
            "last_name": "lastname",
            "email": "manager@gmail.com",
        })
        manager_group = Group.objects.get(name="Office Manager")
        manager_group.user_set.add(user)
        instance = form.save(commit=False)
        instance.user_id = user.id
        instance.save()

        user_form = BaseUserForm({"username": "doctor", "password": "1234"})
        user = user_form.save(commit=False)
        user.set_password(user_form.cleaned_data["password"])
        user.save()
        form = OphthalmologistUserForm({
            "first_name": "firstname",
            "last_name": "lastname",
            "email": "manager@gmail.com",
            "gender": "Male",
        })
        doctor_group = Group.objects.get(name="Ophthalmologist")
        doctor_group.user_set.add(user)
        instance = form.save(commit=False)
        instance.user_id = user.id
        instance.save()
