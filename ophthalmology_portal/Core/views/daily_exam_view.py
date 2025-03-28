import datetime
from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render

from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView


class DailyExamsView(BaseView):
    def get(self, request, *args, **kwargs):
        if not self.manager_verification(request.user) or not self.doctor_verification(request.user):
            raise Http404
        for key in request.GET:
            if request.GET[key] == "Move to Waiting":
                exam = ExamModel.objects.get(id=key)
                exam.in_lobby()
            elif request.GET[key] == "Move to in Progress":
                exam = ExamModel.objects.get(id=key)
                exam.in_progress()
            elif request.GET[key] == "Move to Complete":
                exam = ExamModel.objects.get(id=key)
                exam.complete()
            elif request.GET[key] == "Cancel":
                exam = ExamModel.objects.get(id=key)
                exam.cancel()
        exams = ExamModel.objects.filter(date=datetime.date.today()).reverse()
        paginator = Paginator(exams, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "daily_exam_list.html",
            {
                "page_obj": page_obj,
                "base_template_name": self.get_base_template(request.user),
            },
        )
