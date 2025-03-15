from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render

from ophthalmology_portal.Core.views.base_view import BaseView


class HomePageView(BaseView):

    def get(self, request, *args, **kwargs):
        # TODO: turn this into something useful

        return render(request, "home.html", context={"base_template_name": self.get_base_template(request.user)})
