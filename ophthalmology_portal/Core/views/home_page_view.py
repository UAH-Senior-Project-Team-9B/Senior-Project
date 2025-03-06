from django.http import HttpResponse

from ophthalmology_portal.Core.views.base_view import BaseView


class HomePageView(BaseView):
    def get(self, request, *args, **kwargs):
        # TODO: turn this into something useful
        return HttpResponse("Hello, World!")
