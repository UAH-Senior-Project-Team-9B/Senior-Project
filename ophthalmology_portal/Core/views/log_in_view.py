from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from ophthalmology_portal.Core.forms import (
    BaseUserForm,
    PatientUserForm,
)


class LogInView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = BaseUserForm()
        return render(
            request=request, template_name="log_in.html", context={"form": form}
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request=request, message="Invalid Username")
            return redirect("/login/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request=request, message="Username or password is not valid")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect(reverse("home_page"))


class RegistrationView(View):
    def get(self, request: HttpRequest, token=None, *args, **kwargs):
        form = BaseUserForm()
        return render(
            request=request,
            template_name="base_registration_template.html",
            context={"form": form},
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        form = BaseUserForm(request.POST)
        if form.is_valid():
            request.session["username"] = username
            request.session["password"] = password
            return redirect(reverse("patient_registration"))
        messages.error(request=request, message="wrong")
        return redirect(reverse("registration"))


class PatientRegistrationView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not request.session.__contains__(
            "username"
        ) or not request.session.__contains__("password"):
            return redirect(reverse("registration"))
        form = PatientUserForm()
        return render(request, "patient_registration_template.html", {"form": form})

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.session.pop("username")
        password = request.session.pop("password")
        if User.objects.filter(username=username).exists():
            messages.error(request=request, message="Username Is Taken")
            return redirect("/registration/")
        user_form = BaseUserForm({"username": username, "password": password})
        user = user_form.save(commit=False)
        user.set_password(user_form.cleaned_data["password"])
        user.save()
        form = PatientUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = user.id
            instance.save()
            return redirect("/login/")

        return redirect("/registration/information/")
