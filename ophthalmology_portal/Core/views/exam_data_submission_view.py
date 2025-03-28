from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import (
    OccularExamCreationForm,
    VisualAccuityCreationForm,
)
from ophthalmology_portal.Core.views.base_view import BaseView
from django.http import Http404

# this is for testing purposes, delete this later
class TestInformationCreationView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        visual_form = VisualAccuityCreationForm
        occular_form = OccularExamCreationForm
        return render(
            request=request,
            template_name="exam_data_submission_template.html",
            context={
                "visual_form": visual_form,
                "occular_form": occular_form,
                "base_template_name": self.get_base_template(request.user),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        if not self.doctor_verification(request.user):
            raise Http404
        form = VisualAccuityCreationForm(request.POST)
        form2 = OccularExamCreationForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect(reverse("home_page"))
        return redirect("/create-test-information/")
