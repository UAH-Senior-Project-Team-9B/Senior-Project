from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpRequest
from django.shortcuts import render

from ophthalmology_portal.Core.models import PatientUserModel
from ophthalmology_portal.Core.views.base_view import BaseView


class PatientListView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not self.manager_verification(request.user) and not self.doctor_verification(
            request.user
        ):
            raise Http404
        if "HX-target" in request.headers:
            patients = PatientUserModel.objects.filter(
                Q(first_name__icontains=request.GET["search"])
                | Q(last_name__icontains=request.GET["search"])
            )
            template_name = "patient_list_element.html"
        else:
            patients = PatientUserModel.objects.all()
            template_name = "patient_list.html"
        paginator = Paginator(patients, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            template_name,
            {
                "page_obj": page_obj,
                "base_template_name": self.get_base_template(request.user),
            },
        )
