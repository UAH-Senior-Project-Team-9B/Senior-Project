from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View


class HomePageView(LoginRequiredMixin, View):
    # TODO (LOGAN): Move this into a base view
    redirect_field_name = "redirect"
    redirect_authenticated_user = True
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        # TODO: turn this into something useful
        return HttpResponse("Hello, World!")
