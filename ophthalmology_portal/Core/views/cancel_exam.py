from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse

from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.models.user_models import PatientUserModel
from ophthalmology_portal.Core.views.base_view import BaseView


class CancelExam(BaseView):
    def get(self, request, exam_id, return_page, *args, **kwargs):
        if not self.manager_verification(
            request.user
        ) and not self.patient_verification(request.user):
            raise Http404
        exam = ExamModel.objects.get(id=exam_id)
        if request.user.has_perm("Core.patient"):
            try:
                exam = ExamModel.objects.get(
                    id=exam_id, patient=PatientUserModel.objects.get(user=request.user)
                )
            except:
                raise Http404
        if exam.status != ExamModel.status_choices["complete"]:
            exam.delete()
        else:
            raise Http404
        if return_page == "True":
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            return redirect(reverse("home_page"))
