import datetime

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import ExamCreationMainForm, ExamCreationPostForm
from ophthalmology_portal.Core.models import ExamModel, OphthalmologistUserModel
from ophthalmology_portal.Core.views.base_view import BaseView
from django.http import Http404

# this is for testing purposes, delete this later
class ExamCreationView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404
        form = ExamCreationMainForm
        options = {
            f"{datetime.time(8)}": "8:00 AM",
            f"{datetime.time(8, 30)}": "8:30 AM",
            f"{datetime.time(9)}": "9:00 AM",
            f"{datetime.time(9, 30)}": "9:30 AM",
            f"{datetime.time(10)}": "10:00 AM",
            f"{datetime.time(10, 30)}": "10:30 AM",
            f"{datetime.time(11)}": "11:00 AM",
            f"{datetime.time(11, 30)}": "11:30 AM",
            f"{datetime.time(12)}": "12:00 PM",
            f"{datetime.time(12, 30)}": "12:30 PM",
            f"{datetime.time(13)}": "1:00 PM",
            f"{datetime.time(13, 30)}": "1:30 PM",
            f"{datetime.time(14)}": "2:00 PM",
            f"{datetime.time(14, 30)}": "2:30 PM",
            f"{datetime.time(15)}": "3:00 PM",
            f"{datetime.time(15, 30)}": "3:30 PM",
            f"{datetime.time(16)}": "4:00 PM",
            f"{datetime.time(16, 30)}": "4:30 PM",
            f"{datetime.time(17)}": "5:00 PM",
        }
        doctors = OphthalmologistUserModel.objects.all()
        minimum = datetime.date.today().strftime("%Y-%m-%d")
        maximum = datetime.date.today() + datetime.timedelta(days=2 * 365)
        maximum = maximum.strftime("%Y-%m-%d")
        if "HX-target" in request.headers:
            template_name = "time_submission.html"
            if not request.GET["date"] or not request.GET["doctor"]:
                pass
            else:
                already_taken = ExamModel.objects.filter(
                    date=request.GET["date"],
                    doctor=request.GET["doctor"],
                )
                for i in already_taken:
                    options.pop(f"{i.time}")
        else:
            template_name = "manager_exam_creation_template.html"

        return render(
            request=request,
            template_name=template_name,
            context={
                "form": form,
                "options": options,
                "doctors": doctors,
                "base_template_name": self.get_base_template(request.user),
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404
        if datetime.date.today() >= datetime.datetime.strptime(
            request.POST["date"], "%Y-%m-%d"
        ).date() or datetime.datetime.strptime(
            request.POST["date"], "%Y-%m-%d"
        ).date() >= (datetime.date.today() + datetime.timedelta(days=2 * 365)):
            return redirect("/create-exam/")
        form = ExamCreationPostForm(request.POST)
        if form.is_valid():
            form.status = "upcoming"
            form.save()
            return redirect(reverse("home_page"))
        return redirect("/create-exam/")
