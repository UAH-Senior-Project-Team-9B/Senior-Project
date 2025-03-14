from django.core.paginator import Paginator
from ophthalmology_portal.Core.models import PatientUserModel, ExamModel
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from ophthalmology_portal.Core.forms import ExamCreationPostForm

from django.urls import reverse

class ExamDetailsView(View):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        form = ExamCreationPostForm(instance=ExamModel.objects.get(id=exam_id))
        breakpoint()
        return render(request, "view_exam.html", {"form": form})
