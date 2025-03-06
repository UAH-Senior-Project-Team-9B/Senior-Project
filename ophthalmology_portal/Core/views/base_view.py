from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class BaseView(LoginRequiredMixin, View):
    # TODO (LOGAN): Move this into a base view
    redirect_field_name = "redirect"
    redirect_authenticated_user = True
    login_url = "/login/"
