from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from django.urls import reverse
from ophthalmology_portal.Core.forms import PrescriptionCreationForm


# this is for testing purposes, delete this later
class PrescriptionCreationView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        form = PrescriptionCreationForm
        return render(
            request=request,
            template_name="prescription_creation_template.html",
            context={"form": form},
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = PrescriptionCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("home_page"))
        return redirect("/create-prescription/")
