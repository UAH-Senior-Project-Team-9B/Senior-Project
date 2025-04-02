from django.core.paginator import Paginator
from django.http import Http404, HttpRequest
from django.shortcuts import render

from ophthalmology_portal.Core.models import PatientUserModel, PrescriptionModel
from ophthalmology_portal.Core.views.base_view import BaseView


class PrescriptionListView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        # TODO: Revisit the security logic for this page
        if not self.patient_verification(request.user):
            raise Http404
        patient = request.user.patientusermodel.id
        prescriptions = PrescriptionModel.objects.filter(
            patient=PatientUserModel.objects.get(id=patient)
        )
        paginator = Paginator(prescriptions, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "prescription_list_template.html",
            {
                "page_obj": page_obj,
                "patient": patient,
                "base_template_name": self.get_base_template(request.user),
            },
        )
