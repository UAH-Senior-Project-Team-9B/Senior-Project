from django.contrib import admin

from .models import AppointmentRequest


@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "appointment_date", "appointment_time")
    list_filter = ("appointment_date",)
    search_fields = ("first_name", "last_name")
