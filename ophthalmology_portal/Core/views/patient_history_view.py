from django.core.paginator import Paginator
from django.http import Http404, HttpRequest
from django.shortcuts import render

from ophthalmology_portal.Core.models import ExamModel, PatientUserModel
from ophthalmology_portal.Core.views.base_view import BaseView


class PatientExamHistoryView(BaseView):
    def get(self, request: HttpRequest, patient=None, *args, **kwargs):
        # Security needed
        if not patient:
            if self.patient_verification(request.user):
                patient = request.user.patientusermodel.id
            else:
                raise Http404
        else:
            if not self.manager_verification(
                request.user
            ) and not self.doctor_verification(request.user):
                raise Http404
        exams = ExamModel.objects.filter(
            patient=PatientUserModel.objects.get(id=patient)
        )
        patient_obj = PatientUserModel.objects.get(id=patient)
        paginator = Paginator(exams, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "exam_list.html",
            {
                "page_obj": page_obj,
                "patient": patient,
                "patient_obj": patient_obj,
                "base_template_name": self.get_base_template(request.user),
            },
        )
