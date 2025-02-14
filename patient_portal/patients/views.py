from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import PatientForm

def patient_registration(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_success')
    else:
        form = PatientForm()

    return render(request, 'patients/patient_registration.html', {'form': form})

def patient_success(request):
    return render(request, 'patients/patient_success.html')
