import datetime
from zoneinfo import ZoneInfo

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView
from django.shortcuts import redirect

class CancelExam(BaseView):
    def get(self, request, exam_id, *args, **kwargs):
        if not self.manager_verification(request.user) and not self.patient_verification(request.user):
            raise Http404
        exam = ExamModel.objects.get(id=exam_id)
        if exam.status != "Complete":
            exam.cancel()
        else:
            raise Http404
        return redirect(reverse("home_page"))
