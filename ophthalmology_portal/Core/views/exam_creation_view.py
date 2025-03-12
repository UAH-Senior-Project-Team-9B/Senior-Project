from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from django.urls import reverse
from ophthalmology_portal.Core.forms.exam_creation_form import ExamCreationDateForm, ExamCreationMainForm, ExamCreationPostForm

options = {
    "8:00": "8:00 AM",
    "8:30": "8:30 AM",
    "9:00": "9:00 AM",
    "9:30": "9:30 AM",
    "10:00": "10:00 AM",
    "10:30": "10:30 AM",
    "11:00": "11:00 AM",
    "11:30": "11:30 AM",
    "12:00": "12:00 PM",
    "12:30": "12:30 PM",
    "13:00": "1:00 PM",
    "13:30": "1:30 PM",
    "14:00": "2:00 PM",
    "14:30": "2:30 PM",
    "15:00": "3:00 PM",
    "15:30": "3:30 PM",
    "16:00": "4:00 PM",
    "16:30": "4:30 PM",
    "17:00": "5:00 PM",
}

# this is for testing purposes, delete this later
class ExamCreationView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        breakpoint()
        form = ExamCreationMainForm
        form2 = ExamCreationDateForm
        if "HX-target" in request.headers:
            template_name="test_template.html"
        else:
            template_name="exam_creation_template.html"
        return render(
            request=request, template_name=template_name, context={"form": form, "form2": form2, "options": options}
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = ExamCreationPostForm(request.POST)
        breakpoint()
        if form.is_valid():
            form.save()
            return redirect(reverse("home_page"))
        return redirect("/create-exam/")
