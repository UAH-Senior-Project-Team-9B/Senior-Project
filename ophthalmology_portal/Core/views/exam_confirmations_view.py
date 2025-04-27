from django.core.paginator import Paginator
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render

from ophthalmology_portal.Core.models import ExamModel
from ophthalmology_portal.Core.views.base_view import BaseView


class ExamConfirmationsView(BaseView):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not self.manager_verification(request.user):
            return Http404
        exams = ExamModel.objects.filter(status=ExamModel.status_choices["pending"])
        paginator = Paginator(exams, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(
            request=request,
            template_name="exam_confirmations_template.html",
            context={
                "page_obj": page_obj,
                "base_template_name": self.get_base_template(request.user),
            },
        )

    def post(self, request: HttpRequest, id, *args, **kwargs):
        if not self.manager_verification(request.user):
            raise Http404

        return redirect("/create-exam/")
