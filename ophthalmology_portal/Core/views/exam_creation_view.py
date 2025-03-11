from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from django.urls import reverse
from ophthalmology_portal.Core.forms import ExamCreationForm


# this is for testing purposes, delete this later
class ExamCreationView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        form = ExamCreationForm
        return render(
            request=request, template_name="exam_creation_template.html", context={"form": form}
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = ExamCreationForm(request.POST)
        breakpoint()
        if form.is_valid():
            form.save()
            return redirect(reverse("home_page"))
        return redirect("/create-exam/")
