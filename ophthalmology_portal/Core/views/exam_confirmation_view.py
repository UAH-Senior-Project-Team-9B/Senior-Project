import datetime

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from ophthalmology_portal.Core.forms import ExamCreationMainForm, ExamCreationPostForm
from ophthalmology_portal.Core.forms.exam_creation_form import ExamManagerViewForm
from ophthalmology_portal.Core.forms.prescription_creation_form import PrescriptionViewForm
from ophthalmology_portal.Core.models import ExamModel, OphthalmologistUserModel
from ophthalmology_portal.Core.views.base_view import BaseView
from django.http import Http404

# this is for testing purposes, delete this later
class ExamConfirmationView(BaseView):
    def get(self, request: HttpRequest, id, *args, **kwargs):
        if not self.manager_verification(request.user):
            return Http404
        form = ExamManagerViewForm(instance=ExamModel.objects.get(id=id))
        return render(
            request,
            "pending_exam_template.html",
            {
                "form": form,
                "base_template_name": self.get_base_template(request.user),
                "upload": False,
            },
        )

    def post(self, request: HttpRequest, id, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404
        instance= ExamModel.objects.get(id=id)
        instance.status="upcoming"
        instance.save()
        return redirect("/exam-confirmations/")
