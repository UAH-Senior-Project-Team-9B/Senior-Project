from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import PrescriptionCreationForm
from ophthalmology_portal.Core.views.base_view import BaseView
from django.http import Http404

# this is for testing purposes, delete this later
class PrescriptionCreationView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        form = PrescriptionCreationForm
        return render(
            request=request,
            template_name="prescription_creation_template.html",
            context={
                "form": form,
                "base_template_name": self.get_base_template(request.user),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        form = PrescriptionCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("home_page"))
        return redirect("/create-prescription/")
