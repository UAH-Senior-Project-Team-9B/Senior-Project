from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView
import datetime


class DailyExamsView(BaseView):

    def get(self, request, *args, **kwargs):
        # TODO: turn this into something useful
        exams=ExamModel.objects.filter(date=datetime.date.today()).reverse()
        paginator = Paginator(exams,3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "exam_list.html", {"page_obj": page_obj, "base_template_name": self.get_base_template(request.user)})
