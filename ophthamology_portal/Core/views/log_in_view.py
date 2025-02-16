from ophthamology_portal.Core.forms import PatientUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from ophthamology_portal.Core.forms import BaseUserForm

class LogInView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = BaseUserForm()
        return render(request=request, template_name="log_in.html", context={"form": form})

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request=request, message="Invalid Username")
            return redirect("/login/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request=request, message="Invalid Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/home/")


class RegistrationView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        form = BaseUserForm()
        return render(request=request, template_name="patient_registration_template.html", context={"form": form})

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        form = BaseUserForm(request.POST)
        if form.is_valid():
            request.session["username"] = username
            request.session["password"] = password
            return redirect("/registration/information/")
        messages.error(request=request, message="wrong")
        return redirect("/registration/")



class RegistrationInformationView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        form = PatientUserForm()
        return render(request, "patient_registration_template.html", {"form": form})

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.session["username"]
        password = request.session["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request=request, message="Username Is Taken")
            return redirect("/registration/")
        breakpoint()
        form = PatientUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient_success")

        return redirect("/patient_info/")
