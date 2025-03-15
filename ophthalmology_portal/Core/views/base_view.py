from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View


class BaseView(LoginRequiredMixin, View):
    # TODO (LOGAN): Move this into a base view
    redirect_field_name = "redirect"
    redirect_authenticated_user = True
    login_url = "/login/"

    def get_base_template(self, user: User):
        if user.has_perm("Core.patient"):
            return "base_patient.html"
        elif user.has_perm("Core.doctor"):
            return "base_doctor.html"
        elif user.has_perm("Core.manager"):
            return "base_manager.html"
