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
        if not self.manager_verification(request.user) and not self.patient_verification(request.user):
            raise Http404
        exam = ExamModel.objects.get(id=exam_id)
        if exam.status == "Upcoming":
            exam.in_lobby()
        elif exam.status == 'In Wait Room':
            exam.in_progress()
        elif exam.status == "Exam In Progress":
            if exam.occular_exam_information and exam.visual_accuity_information:
                exam.complete()
            else:
                messages.add_message(request, messages.ERROR, "Exam data not updated.")


        else:
            raise Http404
        return redirect(request.META.get('HTTP_REFERER'))
