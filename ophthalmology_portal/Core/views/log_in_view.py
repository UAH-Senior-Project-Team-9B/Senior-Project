from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from ophthalmology_portal.Core.forms import (
    BaseUserForm,
    PatientUserForm,
    EmergencyContactForm,
    InsuranceProviderForm
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


class PatientInformationRegistrationView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not request.session.__contains__(
            "username"
        ) or not request.session.__contains__("password"):
            return redirect(reverse("registration"))
        form = PatientUserForm()
        form2 = EmergencyContactForm()
        form3 = InsuranceProviderForm()
        return render(request, "patient_registration_template.html", {"form": form,"form2": form2,"form3": form3,})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = PatientUserForm(request.POST)
        form2 = EmergencyContactForm(request.POST)
        form3 = InsuranceProviderForm(request.POST)
        if  request.session.__contains__(
            "username"
        ) or  request.session.__contains__("password"):
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                username = request.session.pop("username")
                password = request.session.pop("password")
                if User.objects.filter(username=username).exists():
                    messages.error(request=request, message="Username Is Taken")
                    return redirect("/registration/")
                user_form = BaseUserForm({"username": username, "password": password})
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data["password"])
                user.save()
                my_group = Group.objects.get(name="Patients")
                my_group.user_set.add(user)
                instance = form.save(commit=False)
                instance.user_id = user.id
                instance.save()
                instance2 = form2.save(commit=False)
                instance2.patient_id = instance.id
                instance2.save()
                instance3 = form3.save(commit=False)
                instance3.patient_id = instance.id
                instance3.save()
                return redirect("/login/")
            for field in form.errors:
                messages.error(request, form.errors[field])
            for field in form2.errors:
                messages.error(request, form2.errors[field])
            for field in form3.errors:
                messages.error(request, form3.errors[field])
            return redirect("/registration/information/")
        else:
            return redirect("/registration/")
