from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse

from ophthalmology_portal.Core.forms import (
    OccularExamCreationForm,
    VisualAccuityCreationForm,
)


# this is for testing purposes, delete this later
class TestInformationCreationView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        form = VisualAccuityCreationForm
        form2 = OccularExamCreationForm
        return render(
            request=request,
            template_name="test_information_creation_template.html",
            context={"form": form, "form2": form2},
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = VisualAccuityCreationForm(request.POST)
        form2 = OccularExamCreationForm(request.POST)
        # breakpoint()
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect(reverse("home_page"))
        return redirect("/create-test-information/")
