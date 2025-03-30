from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from ophthalmology_portal.Core.models import PatientUserModel
from ophthalmology_portal.Core.views.base_view import BaseView
from django.http import Http404

class PatientListView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not self.manager_verification(request.user) and not self.doctor_verification(request.user):
            raise Http404
        patients = PatientUserModel.objects.all()
        paginator = Paginator(patients, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "patient_list.html",
            {
                "page_obj": page_obj,
                "base_template_name": self.get_base_template(request.user),
            },
        )
