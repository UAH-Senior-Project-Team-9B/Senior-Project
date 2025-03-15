from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from django.urls import reverse
from ophthalmology_portal.Core.forms import PrescriptionCreationForm
from ophthalmology_portal.Core.views.base_view import BaseView


# this is for testing purposes, delete this later
class PrescriptionCreationView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        form = PrescriptionCreationForm
        return render(
            request=request,
            template_name="prescription_creation_template.html",
            context={"form": form, "base_template_name": self.get_base_template(request.user)},
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = PrescriptionCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("home_page"))
        return redirect("/create-prescription/")
