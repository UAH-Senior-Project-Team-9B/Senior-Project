from django.shortcuts import redirect, render

from ophthalmology_portal.Core.forms import AppointmentRequestForm


def appointment_request_page(request):
    if request.method == "POST":
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("appointment_success")  # Redirect to success page
    else:
        form = AppointmentRequestForm()

    return render(request, "appointment_request.html", {"form": form})


# ADD THIS FUNCTION
def appointment_success(request):
    return render(request, "appointment_success.html")
