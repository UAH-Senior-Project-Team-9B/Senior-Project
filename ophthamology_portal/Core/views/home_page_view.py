from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View


class HomePageView(LoginRequiredMixin, View):
    redirect_field_name = "redirect"
    redirect_authenticated_user = True
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
