from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ophthamology_portal.Core"

    def ready(self):
        from django.contrib.auth.models import Group  # Prevents circular import

        Group.objects.get_or_create(name="Patients")
        Group.objects.get_or_create(name="Office Manager")
        Group.objects.get_or_create(name="Ophthalmologist")
