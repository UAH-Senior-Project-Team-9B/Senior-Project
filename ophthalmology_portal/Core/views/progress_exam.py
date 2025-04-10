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
from django.contrib import messages

class ProgressExam(BaseView):
    def get(self, request, exam_id, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404

        exam = ExamModel.objects.get(id=exam_id)
        if exam.status == ExamModel.status_choices['upcoming']:
            exam.in_lobby()
        elif exam.status == ExamModel.status_choices['waiting']:
            exam.in_progress()
        elif exam.status == ExamModel.status_choices['progressing']:
            complete = exam.complete()
            if not complete:
                messages.warning(request, "Exams that have not been completed by an Ophthalmogist can not be ended early.")
        else:
            raise Http404
        return redirect(request.META.get('HTTP_REFERER'))
