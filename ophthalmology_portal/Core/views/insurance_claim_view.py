from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from ophthalmology_portal.Core.forms import InsuranceClaimForm
from ophthalmology_portal.Core.forms.exam_creation_form import ExamViewForm
from ophthalmology_portal.Core.forms.patient_info_form import (
    InsuranceProviderViewOnlyForm,
)
from ophthalmology_portal.Core.models.exam_model import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView


class InsuranceClaimView(BaseView):
    def get(self, request: HttpRequest, exam_id, *args, **kwargs):
        if self.patient_verification(request.user):
            raise Http404

        exam = ExamModel.objects.get(id=exam_id)
        try:
            claim = InsuranceClaimForm(instance=exam.insuranceclaimmodel)
        except:
            claim = InsuranceClaimForm()
        form = ExamViewForm(instance=exam)
        insurance_provider_form = InsuranceProviderViewOnlyForm(
            instance=exam.patient.insuranceprovidermodel
        )
        return render(
            request,
            "insurance_claim_view_template.html",
            {
                "form": form,
                "exam": exam,
                "claim": claim,
                "insurance_provider_form": insurance_provider_form,
                "base_template_name": self.get_base_template(request.user),
            },
        )

    def post(self, request: HttpRequest, exam_id, *args, **kwargs):
        if self.patient_verification(request.user):
            raise Http404
        exam = ExamModel.objects.get(id=exam_id)
        claim = InsuranceClaimForm(request.POST)
        if claim.is_valid():
            claim_obj = claim.save(commit=False)
            try:
                breakpoint()
                exam.insuranceclaimmodel.delete()
            except:
                pass
            claim_obj.exam = exam
            claim_obj.save()

            return redirect(reverse("exam_details", kwargs={"exam_id": exam_id}))
        return redirect(reverse("insurance_claim", kwargs={"exam_id": exam_id}))
