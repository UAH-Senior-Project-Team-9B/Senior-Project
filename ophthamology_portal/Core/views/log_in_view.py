from datetime import datetime, timedelta
from secrets import token_urlsafe

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from ophthamology_portal.Core.forms import BaseUserForm, PatientUserForm, TokenAuthForm
from ophthamology_portal.Core.models import TokenAuthModel


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
            messages.error(request=request, message="Invalid Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/home/")


class RegistrationView(View):
    def get(self, request: HttpRequest, token=None, *args, **kwargs):
        form = BaseUserForm()
        if TokenAuthModel.objects.filter(token=token).exists():
            token_obj = TokenAuthModel.objects.get(token=token)
            if token_obj.group == "Office Manager":
                return render(
                    request=request,
                    template_name="office_manager_registration_template.html",
                    context={"form": form},
                )
            if token_obj.group == "Ophthalmologist":
                return render(
                    request=request,
                    template_name="ophtjalmologist_registration_template.html",
                    context={"form": form},
                )

        return render(
            request=request,
            template_name="patient_registration_template.html",
            context={"form": form},
        )

    def post(self, request: HttpRequest, token, *args, **kwargs):
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
        if not request.session.__contains__(
            "username"
        ) or not request.session.__contains__("password"):
            return redirect("/registration/")
        form = PatientUserForm()
        return render(request, "patient_registration_template.html", {"form": form})

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.session["username"]
        password = request.session["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request=request, message="Username Is Taken")
            return redirect("/registration/")
        form = PatientUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=username, password=password, email=form["email"].value()
            )
            instance = form.save(commit=False)
            instance.user_id = user.id
            instance.save()
            return redirect("/login/")

        return redirect("/registration/information/")


class TokenGenerationView(View):
    def get(self, request):
        form = TokenAuthForm()
        return render(request, "token_gen.html", {"form": form})

    def post(self, request):
        form = TokenAuthForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.time_created = datetime.now()
            instance.expiration = instance.time_created + timedelta(days=2)
            instance.token = token_urlsafe(16)
            instance.save()
            messages.info(
                request=request, message="Token generated successfully, copy below"
            )
            return render(request, "token_gen.html", {"token": instance.token})
        messages.error(request=request, message="something went wrong")
        return render(request, "token_gen.html")
