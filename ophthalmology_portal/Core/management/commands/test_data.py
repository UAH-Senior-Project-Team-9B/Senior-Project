from django.contrib.auth.models import (
    Group,
    Permission,
)
from django.core.management.base import BaseCommand

from ophthalmology_portal.Core.forms import (
    ManagerUserForm,
    OphthalmologistUserForm,
    PatientUserForm,
    EmergencyContactForm,
    InsuranceProviderForm,
    BaseUserForm,
    ExamCreationPostForm,
)
from django.contrib.auth.models import User
import datetime
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from ophthalmology_portal.Core.forms.prescription_creation_form import PrescriptionCreationForm
from ophthalmology_portal.Core.forms.test_information_creation_form import OccularExamCreationForm, VisualAccuityCreationForm
from ophthalmology_portal.Core.models.user_models import OphthalmologistUserModel

class Command(BaseCommand):
    help = "Generates data used for debugging. DO NOT RUN IN DEVELOPMENT."

    def handle(self, *args, **options):
        patient_group, patient_group_exists = Group.objects.get_or_create(name="Patients")
        manager_group, manager_group_exists = Group.objects.get_or_create(
            name="Office Manager"
        )
        doctor_group, doctor_exists = Group.objects.get_or_create(
            name="Ophthalmologist"
        )
        if patient_group_exists:
            for permission in Permission.objects.filter(name="Patient Permissions"):
                patient_group.permissions.add(permission)
        if manager_group_exists:
            for permission in Permission.objects.filter(name="Manager Permissions"):
                manager_group.permissions.add(permission)
        if doctor_exists:
            for permission in Permission.objects.filter(name="Doctor Permissions"):
                doctor_group.permissions.add(permission)




        if not User.objects.filter(username="manager"):

            user_form = BaseUserForm({"username": "manager", "password": "1234"})
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            form = ManagerUserForm({
                "first_name": "Toasty",
                "last_name": "Moe",
                "email": "manager@gmail.com",
            })
            manager_group.user_set.add(user)
            patient = form.save(commit=False)
            patient.user_id = user.id
            patient.save()


        if not User.objects.filter(username="doctor"):
            user_form = BaseUserForm({"username": "doctor", "password": "1234"})
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            form = OphthalmologistUserForm({
                "first_name": "Scott",
                "last_name": "Fitzgerald",
                "email": "greatgatsby@gmail.com",
                "gender": "Male",
            })
            doctor_group.user_set.add(user)
            doctor = form.save(commit=False)
            doctor.user_id = user.id
            doctor.save()
        else:
            doctor = OphthalmologistUserModel(user=User.objects.get(username="doctor"))

        if not User.objects.filter(username="doctor2"):
            user_form = BaseUserForm({"username": "doctor2", "password": "1234"})
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            form = OphthalmologistUserForm({
                "first_name": "Viktor",
                "last_name": "Frankenstein",
                "email": "frankenstein@gmail.com",
                "gender": "Male",
            })
            doctor_group.user_set.add(user)
            patient = form.save(commit=False)
            patient.user_id = user.id
            patient.save()


        if not User.objects.filter(username="patient"):
            user_form = BaseUserForm({"username": "patient", "password": "1234"})
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            form = PatientUserForm({
                "title": "Mr.",
                "first_name": "John",
                "middle_initial": "j",
                "last_name": "Doe",
                "gender": "Male",
                "date_of_birth": f"{datetime.date.today() - datetime.timedelta(days=23 * 365)}",
                "street_address": "3828 Piermont Dr",
                "city": "Albuquerque",
                "state": "New Mexico",
                "zip_code": "37581",
                "phone_number": "334-123-4567",
                "social_security_number": "111-11-1111",
                "email": "originalman@gmail.com",
            })
            patient_group.user_set.add(user)
            patient = form.save(commit=False)
            patient.user_id = user.id
            patient.save()
            emergency_form = EmergencyContactForm({
                "contact_title": "Mr.",
                "contact_first_name": "Hank",
                "contact_last_name": "Green",
                "contact_relationship": "Friend",
                "contact_phone_number": "334-123-4567",
                "contact_email": "scienceguy123@gmail.com",
            })
            insurance_form = InsuranceProviderForm({
                "insurance_provider": "Blue Cross Blue Shield",
                "contract_number": "1111111111111",
                "group_number": "123141243",
                "effective_date": f"{datetime.date.today() - datetime.timedelta(days=5 * 365)}",
                "co_pay": "5.00",
                "insurance_street_address": "125 insurance street",
                "insurance_city": "Montgomery",
                "insurance_state": "Alabama",
                "insurance_zip_code": "45811",
                "insurance_phone_number": "127-129-3788",
                "primary_care_provider": "Dr. James Norris",
            })
            emergency = emergency_form.save(commit=False)
            insurance = insurance_form.save(commit=False)
            emergency.patient_id=patient.id
            insurance.patient_id=patient.id
            emergency.save()
            insurance.save()
            exam_form = ExamCreationPostForm({
                "date": f"{datetime.date.today()}",
                "time": f"{datetime.time(11, 30)}",
                "patient": patient,
                "doctor": doctor,
                "reason_for_visit": "Eyes be hurtin",
            })
            prescription_form=PrescriptionCreationForm({
                "date_prescribed": f"{datetime.date.today()}",
                "od_cylinder": 0.02,
                "od_sphere": 0.02,
                "od_axis": 0.02,
                "od_add": 0.02,
                "od_prism": 0.02,
                "od_prism_base": 0.02,
                "os_cylinder": 0.02,
                "os_sphere": 0.02,
                "os_axis": 0.02,
                "os_add": 0.02,
                "os_prism": 0.02,
                "os_prism_base": 0.02,
                "visual_acuity": 10,
            })
            left_eye= open('left_eye/test_left_eye.jpg', 'rb')
            right_eye= open('right_eye/test_right_eye.jpg', 'rb')
            file_data={
                "image_of_left_eye": SimpleUploadedFile('left_eye/test_left_eye.jpg', left_eye.read()),
                "image_of_right_eye": SimpleUploadedFile('right_eye/test_right_eye.jpg', right_eye.read()),
            }
            occular_form=OccularExamCreationForm({
                "Vitreous Segment": "CRITICAL",
                "Macula Segment": "CRITICAL",
                "Vasculature Segment": "CRITICAL",
                "Posterior Pole Segment": "CRITICAL",
                "Peripheral Retina Segment": "CRITICAL",
                "Misc Retina Segment": "CRITICAL",
                "Diabeti Eval Segment": "CRITICAL",
                "HTL Evaluation Segment": "CRITICAL",
                "ARMD Segment": "CRITICAL",
                "OS Sponeaneous Venous Pulsation": "+",
                "OD Venous Pulsation": "+",
                "OS Reflex": "+",
                "OD Reflex": "+",
                "Evaluation Performed": "Not Performed",
                "dilated_with_drops": 1,
                "dilated_with_drug": "Atropine",
                "OD Cup-Disc Horizontal Ratio": 0.01,
                "OD Cup-Disc Vertical Ratio": 0.01,
                "OS Cup-Disc Horizontal Ratio": 0.01,
                "OS Cup-Disc Vertical Ratio": 0.01,
                "Optic Nerve": "CRITICAL",
                "Nerve Fiber Layer": "CRITICAL",
            }, file_data)
            visual_form=VisualAccuityCreationForm({
                "distance": "D",
                "OS Visual Accuity": 10,
                "Corrector Indicator": "cc",
                "Right Eye Measurement": 10,
                "OD Corrector Indicator": "cc",
                "OU Visual Accuity": 10,
                "OU Corrector Indicator": "cc",
            })
            exam1=exam_form.save()
            prescription = prescription_form.save(commit=False)
            prescription.prescriber_id = doctor.id
            prescription.save()
            occular = occular_form.save()
            visual = visual_form.save()
            exam1.prescription_id = prescription.id
            exam1.occular_exam_information_id = occular.id
            exam1.visual_accuity_information_id = visual.id

            exam1.save()
            for i in range(1,6):
                exam_form = ExamCreationPostForm({
                    "date": f"{datetime.date.today() - datetime.timedelta(days=i * 30) }",
                    "time": f"{datetime.time(11, 30)}",
                    "patient": patient,
                    "doctor": doctor,
                    "reason_for_visit": "Eyes be hurtin",
                })
                prescription_form=PrescriptionCreationForm({
                    "date_prescribed": f"{datetime.date.today() - datetime.timedelta(days=i * 30)}",
                    "od_cylinder": 0.02,
                    "od_sphere": 0.02,
                    "od_axis": 0.02,
                    "od_add": 0.02,
                    "od_prism": 0.02,
                    "od_prism_base": 0.02,
                    "os_cylinder": 0.02,
                    "os_sphere": 0.02,
                    "os_axis": 0.02,
                    "os_add": 0.02,
                    "os_prism": 0.02,
                    "os_prism_base": 0.02,
                    "visual_acuity": 10,
                })
                left_eye= open('left_eye/test_left_eye.jpg', 'rb')
                right_eye= open('right_eye/test_right_eye.jpg', 'rb')
                file_data={
                    "image_of_left_eye": SimpleUploadedFile('left_eye/test_left_eye.jpg', left_eye.read()),
                    "image_of_right_eye": SimpleUploadedFile('right_eye/test_right_eye.jpg', right_eye.read()),
                }
                occular_form=OccularExamCreationForm({
                    "Vitreous Segment": "CRITICAL",
                    "Macula Segment": "CRITICAL",
                    "Vasculature Segment": "CRITICAL",
                    "Posterior Pole Segment": "CRITICAL",
                    "Peripheral Retina Segment": "CRITICAL",
                    "Misc Retina Segment": "CRITICAL",
                    "Diabeti Eval Segment": "CRITICAL",
                    "HTL Evaluation Segment": "CRITICAL",
                    "ARMD Segment": "CRITICAL",
                    "OS Sponeaneous Venous Pulsation": "+",
                    "OD Venous Pulsation": "+",
                    "OS Reflex": "+",
                    "OD Reflex": "+",
                    "Evaluation Performed": "Not Performed",
                    "dilated_with_drops": 1,
                    "dilated_with_drug": "Atropine",
                    "OD Cup-Disc Horizontal Ratio": 0.01,
                    "OD Cup-Disc Vertical Ratio": 0.01,
                    "OS Cup-Disc Horizontal Ratio": 0.01,
                    "OS Cup-Disc Vertical Ratio": 0.01,
                    "Optic Nerve": "CRITICAL",
                    "Nerve Fiber Layer": "CRITICAL",
                }, file_data)
                visual_form=VisualAccuityCreationForm({
                    "distance": "D",
                    "OS Visual Accuity": 10,
                    "Corrector Indicator": "cc",
                    "Right Eye Measurement": 10,
                    "OD Corrector Indicator": "cc",
                    "OU Visual Accuity": 10,
                    "OU Corrector Indicator": "cc",
                })
                exam1=exam_form.save()
                prescription = prescription_form.save(commit=False)
                prescription.prescriber_id = doctor.id
                prescription.save()
                occular = occular_form.save()
                visual = visual_form.save()
                exam1.prescription_id = prescription.id
                exam1.occular_exam_information_id = occular.id
                exam1.visual_accuity_information_id = visual.id

                exam1.save()



        if not User.objects.filter(username="patient2"):
            user_form = BaseUserForm({"username": "patient2", "password": "1234"})
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            form = PatientUserForm({
                "title": "Mr.",
                "first_name": "Bill",
                "middle_initial": "j",
                "last_name": "Nye",
                "gender": "Male",
                "date_of_birth": f"{datetime.date.today() - datetime.timedelta(days=23 * 365)}",
                "street_address": "3828 Piermont Dr",
                "city": "Albuquerque",
                "state": "New Mexico",
                "zip_code": "37581",
                "phone_number": "334-123-4567",
                "social_security_number": "111-11-1112",
                "email": "scienceguy@gmail.com",
            })

            patient_group.user_set.add(user)
            patient = form.save(commit=False)
            patient.user_id = user.id
            patient.save()
            emergency_form = EmergencyContactForm({
                "contact_title": "Mr.",
                "contact_first_name": "Hank",
                "contact_last_name": "Green",
                "contact_relationship": "Friend",
                "contact_phone_number": "334-123-4567",
                "contact_email": "scienceguy123@gmail.com",
            })
            insurance_form = InsuranceProviderForm({
                "insurance_provider": "Blue Cross Blue Shield",
                "contract_number": "1111111111111",
                "group_number": "123141243",
                "effective_date": f"{datetime.date.today() - datetime.timedelta(days=5 * 365)}",
                "co_pay": "5.00",
                "insurance_street_address": "125 insurance street",
                "insurance_city": "Montgomery",
                "insurance_state": "Alabama",
                "insurance_zip_code": "45811",
                "insurance_phone_number": "127-129-3788",
                "primary_care_provider": "Dr. James Norris",
            })
            emergency = emergency_form.save(commit=False)
            insurance = insurance_form.save(commit=False)
            emergency.patient_id=patient.id
            insurance.patient_id=patient.id
            emergency.save()
            insurance.save()
            exam_form = ExamCreationPostForm({
                "date": f"{datetime.date.today()}",
                "time": f"{datetime.time(12, 30)}",
                "patient": patient,
                "doctor": doctor,
                "reason_for_visit": "Eyes be hurtin",
            })
            exam=exam_form.save(commit=False)
            exam.status="Upcoming"
            exam.save()
            for i in range(1,6):
                exam_form = ExamCreationPostForm({
                    "date": f"{datetime.date.today() - datetime.timedelta(days=i * 30) }",
                    "time": f"{datetime.time(12, 30)}",
                    "patient": patient,
                    "doctor": doctor,
                    "reason_for_visit": "Eyes be hurtin",
                })
                prescription_form=PrescriptionCreationForm({
                    "date_prescribed": f"{datetime.date.today() - datetime.timedelta(days=i * 30)}",
                    "od_cylinder": 0.02,
                    "od_sphere": 0.02,
                    "od_axis": 0.02,
                    "od_add": 0.02,
                    "od_prism": 0.02,
                    "od_prism_base": 0.02,
                    "os_cylinder": 0.02,
                    "os_sphere": 0.02,
                    "os_axis": 0.02,
                    "os_add": 0.02,
                    "os_prism": 0.02,
                    "os_prism_base": 0.02,
                    "visual_acuity": 10,
                })
                left_eye= open('left_eye/test_left_eye.jpg', 'rb')
                right_eye= open('right_eye/test_right_eye.jpg', 'rb')
                file_data={
                    "image_of_left_eye": SimpleUploadedFile('left_eye/test_left_eye.jpg', left_eye.read()),
                    "image_of_right_eye": SimpleUploadedFile('right_eye/test_right_eye.jpg', right_eye.read()),
                }
                occular_form=OccularExamCreationForm({
                    "Vitreous Segment": "CRITICAL",
                    "Macula Segment": "CRITICAL",
                    "Vasculature Segment": "CRITICAL",
                    "Posterior Pole Segment": "CRITICAL",
                    "Peripheral Retina Segment": "CRITICAL",
                    "Misc Retina Segment": "CRITICAL",
                    "Diabeti Eval Segment": "CRITICAL",
                    "HTL Evaluation Segment": "CRITICAL",
                    "ARMD Segment": "CRITICAL",
                    "OS Sponeaneous Venous Pulsation": "+",
                    "OD Venous Pulsation": "+",
                    "OS Reflex": "+",
                    "OD Reflex": "+",
                    "Evaluation Performed": "Not Performed",
                    "dilated_with_drops": 1,
                    "dilated_with_drug": "Atropine",
                    "OD Cup-Disc Horizontal Ratio": 0.01,
                    "OD Cup-Disc Vertical Ratio": 0.01,
                    "OS Cup-Disc Horizontal Ratio": 0.01,
                    "OS Cup-Disc Vertical Ratio": 0.01,
                    "Optic Nerve": "CRITICAL",
                    "Nerve Fiber Layer": "CRITICAL",
                }, file_data)
                visual_form=VisualAccuityCreationForm({
                    "distance": "D",
                    "OS Visual Accuity": 10,
                    "Corrector Indicator": "cc",
                    "Right Eye Measurement": 10,
                    "OD Corrector Indicator": "cc",
                    "OU Visual Accuity": 10,
                    "OU Corrector Indicator": "cc",
                })
                exam1=exam_form.save()
                prescription = prescription_form.save(commit=False)
                prescription.prescriber_id = doctor.id
                prescription.save()
                occular = occular_form.save()
                visual = visual_form.save()
                exam1.prescription_id = prescription.id
                exam1.occular_exam_information_id = occular.id
                exam1.visual_accuity_information_id = visual.id

                exam1.save()

        if not User.objects.filter(username="patient3"):

            user_form = BaseUserForm({"username": "patient3", "password": "1234"})
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            form = PatientUserForm({
                "title": "Mr.",
                "first_name": "Hank",
                "middle_initial": "j",
                "last_name": "Green",
                "gender": "Male",
                "date_of_birth": f"{datetime.date.today() - datetime.timedelta(days=23 * 365)}",
                "street_address": "3828 Piermont Dr",
                "city": "Albuquerque",
                "state": "New Mexico",
                "zip_code": "37581",
                "phone_number": "334-123-4567",
                "social_security_number": "111-11-1113",
                "email": "scienceguy123@gmail.com",
            })

            patient_group.user_set.add(user)
            patient = form.save(commit=False)
            patient.user_id = user.id
            patient.save()
            emergency_form = EmergencyContactForm({
                "contact_title": "Mr.",
                "contact_first_name": "Bill",
                "contact_last_name": "Nye",
                "contact_relationship": "Friend",
                "contact_phone_number": "334-123-4567",
                "contact_email": "scienceguy@gmail.com",
            })
            insurance_form = InsuranceProviderForm({
                "insurance_provider": "Blue Cross Blue Shield",
                "contract_number": "1111111111111",
                "group_number": "123141243",
                "effective_date": f"{datetime.date.today() - datetime.timedelta(days=5 * 365)}",
                "co_pay": "5.00",
                "insurance_street_address": "125 insurance street",
                "insurance_city": "Montgomery",
                "insurance_state": "Alabama",
                "insurance_zip_code": "45811",
                "insurance_phone_number": "127-129-3788",
                "primary_care_provider": "Dr. James Norris",
            })
            emergency = emergency_form.save(commit=False)
            insurance = insurance_form.save(commit=False)
            emergency.patient_id=patient.id
            insurance.patient_id=patient.id
            emergency.save()
            insurance.save()
            exam_form = ExamCreationPostForm({
                "date": f"{datetime.date.today()}",
                "time": f"{datetime.time(3, 30)}",
                "patient": patient,
                "doctor": doctor,
                "reason_for_visit": "Eyes be hurtin",
            })
            exam=exam_form.save(commit=False)
            exam.status="In Progress"
            exam.save()
            for i in range(1,6):
                exam_form = ExamCreationPostForm({
                    "date": f"{datetime.date.today() - datetime.timedelta(days=i * 30) }",
                    "time": f"{datetime.time(10, 30)}",
                    "patient": patient,
                    "doctor": doctor,
                    "reason_for_visit": "Eyes be hurtin",
                })
                prescription_form=PrescriptionCreationForm({
                    "date_prescribed": f"{datetime.date.today() - datetime.timedelta(days=i * 30)}",
                    "od_cylinder": 0.02,
                    "od_sphere": 0.02,
                    "od_axis": 0.02,
                    "od_add": 0.02,
                    "od_prism": 0.02,
                    "od_prism_base": 0.02,
                    "os_cylinder": 0.02,
                    "os_sphere": 0.02,
                    "os_axis": 0.02,
                    "os_add": 0.02,
                    "os_prism": 0.02,
                    "os_prism_base": 0.02,
                    "visual_acuity": 10,
                })
                left_eye= open('left_eye/test_left_eye.jpg', 'rb')
                right_eye= open('right_eye/test_right_eye.jpg', 'rb')
                file_data={
                    "image_of_left_eye": SimpleUploadedFile('left_eye/test_left_eye.jpg', left_eye.read()),
                    "image_of_right_eye": SimpleUploadedFile('right_eye/test_right_eye.jpg', right_eye.read()),
                }
                occular_form=OccularExamCreationForm({
                    "Vitreous Segment": "CRITICAL",
                    "Macula Segment": "CRITICAL",
                    "Vasculature Segment": "CRITICAL",
                    "Posterior Pole Segment": "CRITICAL",
                    "Peripheral Retina Segment": "CRITICAL",
                    "Misc Retina Segment": "CRITICAL",
                    "Diabeti Eval Segment": "CRITICAL",
                    "HTL Evaluation Segment": "CRITICAL",
                    "ARMD Segment": "CRITICAL",
                    "OS Sponeaneous Venous Pulsation": "+",
                    "OD Venous Pulsation": "+",
                    "OS Reflex": "+",
                    "OD Reflex": "+",
                    "Evaluation Performed": "Not Performed",
                    "dilated_with_drops": 1,
                    "dilated_with_drug": "Atropine",
                    "OD Cup-Disc Horizontal Ratio": 0.01,
                    "OD Cup-Disc Vertical Ratio": 0.01,
                    "OS Cup-Disc Horizontal Ratio": 0.01,
                    "OS Cup-Disc Vertical Ratio": 0.01,
                    "Optic Nerve": "CRITICAL",
                    "Nerve Fiber Layer": "CRITICAL",
                }, file_data)
                visual_form=VisualAccuityCreationForm({
                    "distance": "D",
                    "OS Visual Accuity": 10,
                    "Corrector Indicator": "cc",
                    "Right Eye Measurement": 10,
                    "OD Corrector Indicator": "cc",
                    "OU Visual Accuity": 10,
                    "OU Corrector Indicator": "cc",
                })
                exam1=exam_form.save()
                prescription = prescription_form.save(commit=False)
                prescription.prescriber_id = doctor.id
                prescription.save()
                occular = occular_form.save()
                visual = visual_form.save()
                exam1.prescription_id = prescription.id
                exam1.occular_exam_information_id = occular.id
                exam1.visual_accuity_information_id = visual.id
                exam1.save()

        if not User.objects.filter(username="patient4"):

            user_form = BaseUserForm({"username": "patient4", "password": "1234"})
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            form = PatientUserForm({
                "title": "Mr.",
                "first_name": "Joe",
                "middle_initial": "j",
                "last_name": "Mama",
                "gender": "Male",
                "date_of_birth": f"{datetime.date.today() - datetime.timedelta(days=23 * 365)}",
                "street_address": "3828 Piermont Dr",
                "city": "Albuquerque",
                "state": "New Mexico",
                "zip_code": "37581",
                "phone_number": "334-123-4567",
                "social_security_number": "111-11-1114",
                "email": "scienceguy123@gmail.com",
            })

            patient_group.user_set.add(user)
            patient = form.save(commit=False)
            patient.user_id = user.id
            patient.save()
            emergency_form = EmergencyContactForm({
                "contact_title": "Mr.",
                "contact_first_name": "Bill",
                "contact_last_name": "Nye",
                "contact_relationship": "Friend",
                "contact_phone_number": "334-123-4567",
                "contact_email": "scienceguy@gmail.com",
            })
            insurance_form = InsuranceProviderForm({
                "insurance_provider": "Blue Cross Blue Shield",
                "contract_number": "1111111111111",
                "group_number": "123141243",
                "effective_date": f"{datetime.date.today() - datetime.timedelta(days=5 * 365)}",
                "co_pay": "5.00",
                "insurance_street_address": "125 insurance street",
                "insurance_city": "Montgomery",
                "insurance_state": "Alabama",
                "insurance_zip_code": "45811",
                "insurance_phone_number": "127-129-3788",
                "primary_care_provider": "Dr. James Norris",
            })
            emergency = emergency_form.save(commit=False)
            insurance = insurance_form.save(commit=False)
            emergency.patient_id=patient.id
            insurance.patient_id=patient.id
            emergency.save()
            insurance.save()
            exam_form = ExamCreationPostForm({
                "date": f"{datetime.date.today() + datetime.timedelta(days=15)}",
                "time": f"{datetime.time(4, 30)}",
                "patient": patient,
                "doctor": doctor,
                "reason_for_visit": "Eyes be hurtin",
            })
            exam=exam_form.save(commit=False)
            exam.save()
            for i in range(1,6):
                exam_form = ExamCreationPostForm({
                    "date": f"{datetime.date.today() - datetime.timedelta(days=i * 30) }",
                    "time": f"{datetime.time(9, 30)}",
                    "patient": patient,
                    "doctor": doctor,
                    "reason_for_visit": "Eyes be hurtin",
                })
                prescription_form=PrescriptionCreationForm({
                    "date_prescribed": f"{datetime.date.today() - datetime.timedelta(days=i * 30)}",
                    "od_cylinder": 0.02,
                    "od_sphere": 0.02,
                    "od_axis": 0.02,
                    "od_add": 0.02,
                    "od_prism": 0.02,
                    "od_prism_base": 0.02,
                    "os_cylinder": 0.02,
                    "os_sphere": 0.02,
                    "os_axis": 0.02,
                    "os_add": 0.02,
                    "os_prism": 0.02,
                    "os_prism_base": 0.02,
                    "visual_acuity": 10,
                })
                left_eye= open('left_eye/test_left_eye.jpg', 'rb')
                right_eye= open('right_eye/test_right_eye.jpg', 'rb')
                file_data={
                    "image_of_left_eye": SimpleUploadedFile('left_eye/test_left_eye.jpg', left_eye.read()),
                    "image_of_right_eye": SimpleUploadedFile('right_eye/test_right_eye.jpg', right_eye.read()),
                }
                occular_form=OccularExamCreationForm({
                    "Vitreous Segment": "CRITICAL",
                    "Macula Segment": "CRITICAL",
                    "Vasculature Segment": "CRITICAL",
                    "Posterior Pole Segment": "CRITICAL",
                    "Peripheral Retina Segment": "CRITICAL",
                    "Misc Retina Segment": "CRITICAL",
                    "Diabeti Eval Segment": "CRITICAL",
                    "HTL Evaluation Segment": "CRITICAL",
                    "ARMD Segment": "CRITICAL",
                    "OS Sponeaneous Venous Pulsation": "+",
                    "OD Venous Pulsation": "+",
                    "OS Reflex": "+",
                    "OD Reflex": "+",
                    "Evaluation Performed": "Not Performed",
                    "dilated_with_drops": 1,
                    "dilated_with_drug": "Atropine",
                    "OD Cup-Disc Horizontal Ratio": 0.01,
                    "OD Cup-Disc Vertical Ratio": 0.01,
                    "OS Cup-Disc Horizontal Ratio": 0.01,
                    "OS Cup-Disc Vertical Ratio": 0.01,
                    "Optic Nerve": "CRITICAL",
                    "Nerve Fiber Layer": "CRITICAL",
                }, file_data)
                visual_form=VisualAccuityCreationForm({
                    "distance": "D",
                    "OS Visual Accuity": 10,
                    "Corrector Indicator": "cc",
                    "Right Eye Measurement": 10,
                    "OD Corrector Indicator": "cc",
                    "OU Visual Accuity": 10,
                    "OU Corrector Indicator": "cc",
                })
                exam1=exam_form.save()
                prescription = prescription_form.save(commit=False)
                prescription.prescriber_id = doctor.id
                prescription.save()
                occular = occular_form.save()
                visual = visual_form.save()
                exam1.prescription_id = prescription.id
                exam1.occular_exam_information_id = occular.id
                exam1.visual_accuity_information_id = visual.id
                exam1.save()
