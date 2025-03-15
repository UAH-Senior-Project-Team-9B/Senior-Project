from django.core.paginator import Paginator
from ophthalmology_portal.Core.models import PatientUserModel, ExamModel
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from ophthalmology_portal.Core.forms import ExamViewForm

from django.urls import reverse
from ophthalmology_portal.Core.views.base_view import BaseView

class ExamDetailsView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        form = ExamViewForm(instance=ExamModel.objects.get(id=exam_id))

        return render(request, "view_exam.html", {"form": form, "base_template_name": self.get_base_template(request.user)})
