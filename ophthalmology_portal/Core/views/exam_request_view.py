import datetime
from zoneinfo import ZoneInfo

from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import ExamCreationMainForm, ExamCreationPostForm
from ophthalmology_portal.Core.models import ExamModel, OphthalmologistUserModel
from ophthalmology_portal.Core.views.base_view import BaseView


# this is for testing purposes, delete this later
class PatientExamCreationView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not self.patient_verification(request.user):
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
        minimum = datetime.datetime.now(
            ZoneInfo("America/Indiana/Knox")
        ).date() + datetime.timedelta(days=14)
        maximum = datetime.datetime.now(
            ZoneInfo("America/Indiana/Knox")
        ).date() + datetime.timedelta(days=2 * 365)
        minimum = minimum.strftime("%Y-%m-%d")
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
            template_name = "exam_request_template.html"
        return render(
            request=request,
            template_name=template_name,
            context={
                "options": options,
                "doctors": doctors,
                "base_template_name": self.get_base_template(request.user),
                "minimum": minimum,
                "maximum": maximum,
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        if not self.patient_verification(request.user):
            raise Http404
        if datetime.datetime.now(
            ZoneInfo("America/Indiana/Knox")
        ).date() >= datetime.datetime.strptime(
            request.POST["date"], "%Y-%m-%d"
        ).date() or datetime.datetime.strptime(
            request.POST["date"], "%Y-%m-%d"
        ).date() >= (
            datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date()
            + datetime.timedelta(days=2 * 365)
        ):
            return redirect("/exam-request/")
        data = request.POST.copy()
        data["patient"] = request.user.patientusermodel.id
        form = ExamCreationPostForm(data)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.status = ExamModel.status_choices["pending"]
            exam.save()
            return redirect(reverse("home_page"))
        return redirect("/exam-request/")
