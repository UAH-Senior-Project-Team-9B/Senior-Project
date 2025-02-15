from ophthamology_portal.Core.forms import PatientUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View


class LogInView(View):
    def get(request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="log_in.html")

    def post(request: HttpRequest):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request=request, message="Invalid Username")
            return redirect("/login/")

        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request=request, message="Invalid Password")
            return redirect("/login/")
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect("/home/")


class RegistrationView(View):
    def get(request: HttpRequest):
        form = PatientUserForm()
        return render(request, "registration.html", {"form": form})

    def post(request: HttpRequest):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request=request, message="Username Is Taken")
            return redirect("/registration/")
        breakpoint()
        form = PatientUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient_success")

        request.session["username"] = username
        request.session["password"] = password
        return redirect("/patient_info/")
