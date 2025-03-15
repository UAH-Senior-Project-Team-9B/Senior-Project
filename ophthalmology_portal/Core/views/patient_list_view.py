from django.core.paginator import Paginator
from ophthalmology_portal.Core.models import PatientUserModel
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User

from django.urls import reverse
from ophthalmology_portal.Core.views.base_view import BaseView

class PatientListView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        patients=PatientUserModel.objects.all()
        paginator = Paginator(patients,3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "patient_list.html", {"page_obj": page_obj, "base_template_name": self.get_base_template(request.user)})
