from django.core.paginator import Paginator
from ophthalmology_portal.Core.models import PatientUserModel, ExamModel
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User

from django.urls import reverse

class PatientExamHistoryView(View):
    def get(self, request: HttpRequest, patient, *args, **kwargs):
        exams=ExamModel.objects.filter(patient=PatientUserModel.objects.get(id=patient))
        paginator = Paginator(exams,3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "exam_list.html", {"page_obj": page_obj, "patient": patient})
