from django.core.paginator import Paginator
from ophthalmology_portal.Core.models import PatientUserModel, ExamModel
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User

from django.urls import reverse
from ophthalmology_portal.Core.views.base_view import BaseView

class PatientExamHistoryView(BaseView):
    def get(self, request: HttpRequest, patient=None, *args, **kwargs):
        if not patient:
            patient = request.user.patientusermodel.id
            breakpoint()
        exams=ExamModel.objects.filter(patient=PatientUserModel.objects.get(id=patient))
        paginator = Paginator(exams,3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "exam_list.html", {"page_obj": page_obj, "patient": patient, "base_template_name": self.get_base_template(request.user)})
