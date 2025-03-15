from django.contrib.auth.models import User
from ophthalmology_portal.Core import models
from ophthalmology_portal.Core.forms.base_user_form import BaseUserForm
from ophthalmology_portal.Core.forms.user_forms import ManagerUserForm, OphthalmologistUserForm
from django.contrib.auth.models import Group

user_form = BaseUserForm({"username": "patient", "password": "1234"})
user = user_form.save(commit=False)
user.set_password(user_form.cleaned_data["password"])
user.save()
form = ManagerUserForm({"first_name": "firstname", "last_name": "lastname", "email": "manager@gmail.com"})
my_group = Group.objects.get(name='Office Manager')
my_group.user_set.add(user)
instance = form.save(commit=False)
instance.user_id = user.id
instance.save()


user_form = BaseUserForm({"username": "doctor", "password": "1234"})
user = user_form.save(commit=False)
user.set_password(user_form.cleaned_data["password"])
user.save()
form = OphthalmologistUserForm({"first_name": "firstname", "last_name": "lastname", "email": "manager@gmail.com", "gender": "Male"})
my_group = Group.objects.get(name='Ophthalmologist')
my_group.user_set.add(user)
instance = form.save(commit=False)
instance.user_id = user.id
instance.save()

from ophthalmology_portal.Core.forms import ExamCreationMainForm, ExamCreationPostForm
from ophthalmology_portal.Core.models import ExamModel
form = ExamCreationPostForm({'csrfmiddlewaretoken': 'NVK0HGnKLQawOuX2b6lcSDiDwSjjs2w6N8DbcsUgFEKSnd9brkQmt3vEzdRSDP8g', 'patient': '1', 'doctor': '1', 'date': '2025-03-15', 'time': '08:00:00'})
form.is_valid()
form.save()
ExamModel.objects.all()
# exam = ExamModel(date='2025-03-15',time='08:00:00',patient=user_models.PatientUserModel.objects.get(id=1),doctor=user_models.PatientUserModel)
