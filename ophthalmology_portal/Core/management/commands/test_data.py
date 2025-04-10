import datetime
import random
from zoneinfo import ZoneInfo

from django.contrib.auth.models import (
    Group,
    Permission,
    User,
)
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand

from ophthalmology_portal.Core.forms import (
    BaseUserForm,
    EmergencyContactForm,
    ExamCreationPostForm,
    InsuranceProviderForm,
    ManagerUserForm,
    OphthalmologistUserForm,
    PatientUserForm,
)
from ophthalmology_portal.Core.forms.prescription_creation_form import (
    PrescriptionCreationForm,
)
from ophthalmology_portal.Core.forms.test_information_creation_form import (
    OccularExamCreationForm,
    VisualAccuitySubmissionForm,
    BothVisualAccuityCreationForm,
)
from ophthalmology_portal.Core.models.exam_model import ExamModel
from ophthalmology_portal.Core.models.user_models import OphthalmologistUserModel


class Command(BaseCommand):
    help = "Generates data used for debugging. DO NOT RUN IN DEVELOPMENT."

    def handle(self, *args, **options):
        patient_group, patient_group_exists = Group.objects.get_or_create(
            name="Patients"
        )
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
                "date_of_birth": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=23 * 365,)}",
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
                "effective_date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=5 * 365)}",
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
            emergency.patient_id = patient.id
            insurance.patient_id = patient.id
            emergency.save()
            insurance.save()
            exam_form = ExamCreationPostForm({
                "date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date()}",
                "time": f"{datetime.time(11, 30)}",
                "patient": patient,
                "doctor": doctor,
                "reason_for_visit": "Eyes be hurtin",
            })
            prescription_form = PrescriptionCreationForm({
                "date_prescribed": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date()}",
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
            left_eye = open("test_data_images/test_left_eye.jpg", "rb")
            right_eye = open("test_data_images/test_right_eye.jpg", "rb")
            file_data = {
                "image_of_left_eye": SimpleUploadedFile(
                    "test_data_images/test_left_eye.jpg", left_eye.read()
                ),
                "image_of_right_eye": SimpleUploadedFile(
                    "test_data_images/test_right_eye.jpg", right_eye.read()
                ),
            }
            occular_form = OccularExamCreationForm(
                {
                    "vitreous_segment": "CRITICAL",
                    "macula_segment": "CRITICAL",
                    "vasculature_segment": "CRITICAL",
                    "posterior_pole_segment": "CRITICAL",
                    "peripheral_retina_segment": "CRITICAL",
                    "misc_retina_segment": "CRITICAL",
                    "biabeti_eval_segment": "CRITICAL",
                    "htl_eval_segment": "CRITICAL",
                    "armd_segment": "CRITICAL",
                    "left_venous_pulsation": "+",
                    "right_venous_pulsation": "+",
                    "left_foveal_reflex": "+",
                    "right_venous_pulsation": "+",
                    "fundus_record": "Not Performed",
                    "dilated_with_drops": 1,
                    "dilated_with_drug": "Atropine",
                    "od_cup_ratio_horizontal": 0.01,
                    "od_cup_ratio_vertical": 0.01,
                    "os_cup_ratio_horizontal": 0.01,
                    "os_cup_ratio_vertical": 0.01,
                    "optic_nerve": "CRITICAL",
                    "nerve_fiber": "CRITICAL",
                },
                file_data,
            )
            aided_near = VisualAccuitySubmissionForm({
                "visual_acuity_measure_left": 10,
                "visual_acuity_measure_right": 10,
                "visual_acuity_measure_both": 10,
            })
            unaided_near = VisualAccuitySubmissionForm({
                "visual_acuity_measure_left": 10,
                "visual_acuity_measure_right": 10,
                "visual_acuity_measure_both": 10,
            }, prefix="unaided_near")
            pinhole_aided_near = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="aided_ph_near")
            pinhole_unaided_near = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="unaided_ph_near")
            aided_distance = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="aided_distance")
            unaided_distance = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="unaided_near_distance")
            pinhole_aided_distance = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="aided_ph_distance")
            pinhole_unaided_distance = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="unaided_ph_distance")
            prescription = prescription_form.save(commit=False)
            prescription.prescriber_id = doctor.id
            prescription.save()
            occular = occular_form.save()
            exam1 = exam_form.save()

            exam1.prescription_id = prescription.id
            exam1.occular_exam_information_id = occular.id

            exam1.visual_accuity_aided_near = aided_near.save()
            exam1.visual_accuity_unaided_near = unaided_near.save()
            exam1.visual_accuity_pinhole_unaided_near = pinhole_unaided_near.save()
            exam1.visual_accuity_pinhole_aided_near = pinhole_aided_near.save()
            exam1.visual_accuity_aided_distance = aided_distance.save()
            exam1.visual_accuity_unaided_distance = unaided_distance.save()
            exam1.visual_accuity_pinhole_aided_distance = pinhole_aided_distance.save()
            exam1.visual_accuity_pinhole_unaided_distance = pinhole_unaided_distance.save()

            exam1.save()
            prescription.os_visual_acuity_distance = exam1.visual_accuity_aided_string_left_distance
            prescription.od_visual_acuity_distance = exam1.visual_accuity_aided_string_right_distance
            prescription.os_visual_acuity_near = exam1.visual_accuity_aided_string_left_near
            prescription.od_visual_acuity_near = exam1.visual_accuity_aided_string_right_near
            prescription.save()
            for i in range(1, 6):
                exam_form = ExamCreationPostForm({
                    "date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=i * 30)}",
                    "time": f"{datetime.time(11, 30)}",
                    "arrival_time": f"{datetime.time(random.randint(9, 16), random.randint(1, 59))}",
                    "patient": patient,
                    "doctor": doctor,
                    "reason_for_visit": "Eyes be hurtin",
                })
                prescription_form = PrescriptionCreationForm({
                    "date_prescribed": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=i * 30)}",
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
                left_eye = open("test_data_images/test_left_eye.jpg", "rb")
                right_eye = open("test_data_images/test_right_eye.jpg", "rb")
                file_data = {
                    "image_of_left_eye": SimpleUploadedFile(
                        "test_data_images/test_left_eye.jpg", left_eye.read()
                    ),
                    "image_of_right_eye": SimpleUploadedFile(
                        "test_data_images/test_right_eye.jpg", right_eye.read()
                    ),
                }
                occular_form = OccularExamCreationForm(
                    {
                        "vitreous_segment": "CRITICAL",
                        "macula_segment": "CRITICAL",
                        "vasculature_segment": "CRITICAL",
                        "posterior_pole_segment": "CRITICAL",
                        "peripheral_retina_segment": "CRITICAL",
                        "misc_retina_segment": "CRITICAL",
                        "biabeti_eval_segment": "CRITICAL",
                        "htl_eval_segment": "CRITICAL",
                        "armd_segment": "CRITICAL",
                        "left_venous_pulsation": "+",
                        "right_venous_pulsation": "+",
                        "left_foveal_reflex": "+",
                        "right_venous_pulsation": "+",
                        "fundus_record": "Not Performed",
                        "dilated_with_drops": 1,
                        "dilated_with_drug": "Atropine",
                        "od_cup_ratio_horizontal": 0.01,
                        "od_cup_ratio_vertical": 0.01,
                        "os_cup_ratio_horizontal": 0.01,
                        "os_cup_ratio_vertical": 0.01,
                        "optic_nerve": "CRITICAL",
                        "nerve_fiber": "CRITICAL",
                    },
                    file_data,
                )
                aided_near = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                })
                unaided_near = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="unaided_near")
                pinhole_aided_near = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_ph_near")
                pinhole_unaided_near = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_ph_near")
                aided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_distance")
                unaided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_near_distance")
                pinhole_aided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_ph_distance")
                pinhole_unaided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_ph_distance")
                exam1 = exam_form.save()
                prescription = prescription_form.save(commit=False)
                prescription.prescriber_id = doctor.id
                prescription.save()
                occular = occular_form.save()

                exam1.prescription_id = prescription.id
                exam1.occular_exam_information_id = occular.id
                exam1.visual_accuity_aided_near = aided_near.save()
                exam1.visual_accuity_unaided_near = unaided_near.save()
                exam1.visual_accuity_pinhole_unaided_near = pinhole_unaided_near.save()
                exam1.visual_accuity_pinhole_aided_near = pinhole_aided_near.save()
                exam1.visual_accuity_aided_distance = aided_distance.save()
                exam1.visual_accuity_unaided_distance = unaided_distance.save()
                exam1.visual_accuity_pinhole_aided_distance = pinhole_aided_distance.save()
                exam1.visual_accuity_pinhole_unaided_distance = pinhole_unaided_distance.save()


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
                "date_of_birth": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=23 * 365)}",
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
                "effective_date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=5 * 365)}",
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
            emergency.patient_id = patient.id
            insurance.patient_id = patient.id
            emergency.save()
            insurance.save()
            exam_form = ExamCreationPostForm({
                "date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date()}",
                "time": f"{datetime.time(12, 30)}",
                "patient": patient,
                "doctor": doctor,
                "reason_for_visit": "Eyes be hurtin",
            })
            exam = exam_form.save(commit=False)
            exam.status = ExamModel.status_choices['upcoming']
            exam.save()
            for i in range(1, 6):
                exam_form = ExamCreationPostForm({
                    "date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=i * 30)}",
                    "time": f"{datetime.time(12, 30)}",
                    "arrival_time": f"{datetime.time(random.randint(9, 16), random.randint(1, 59))}",
                    "patient": patient,
                    "doctor": doctor,
                    "reason_for_visit": "Eyes be hurtin",
                })
                prescription_form = PrescriptionCreationForm({
                    "date_prescribed": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=i * 30)}",
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
                left_eye = open("test_data_images/test_left_eye.jpg", "rb")
                right_eye = open("test_data_images/test_right_eye.jpg", "rb")
                file_data = {
                    "image_of_left_eye": SimpleUploadedFile(
                        "test_data_images/test_left_eye.jpg", left_eye.read()
                    ),
                    "image_of_right_eye": SimpleUploadedFile(
                        "test_data_images/test_right_eye.jpg", right_eye.read()
                    ),
                }
                occular_form = OccularExamCreationForm(
                    {
                        "vitreous_segment": "CRITICAL",
                        "macula_segment": "CRITICAL",
                        "vasculature_segment": "CRITICAL",
                        "posterior_pole_segment": "CRITICAL",
                        "peripheral_retina_segment": "CRITICAL",
                        "misc_retina_segment": "CRITICAL",
                        "biabeti_eval_segment": "CRITICAL",
                        "htl_eval_segment": "CRITICAL",
                        "armd_segment": "CRITICAL",
                        "left_venous_pulsation": "+",
                        "right_venous_pulsation": "+",
                        "left_foveal_reflex": "+",
                        "right_venous_pulsation": "+",
                        "fundus_record": "Not Performed",
                        "dilated_with_drops": 1,
                        "dilated_with_drug": "Atropine",
                        "od_cup_ratio_horizontal": 0.01,
                        "od_cup_ratio_vertical": 0.01,
                        "os_cup_ratio_horizontal": 0.01,
                        "os_cup_ratio_vertical": 0.01,
                        "optic_nerve": "CRITICAL",
                        "nerve_fiber": "CRITICAL",
                    },
                    file_data,
                )
                visual_form = VisualAccuitySubmissionForm({
                    "distance": "D",
                    "visual_acuity_measure_left": 10,
                    "corrector_indicator_left": "cc",
                    "visual_acuity_measure_right": 10,
                    "corrector_indicator_right": "cc",
                })
                exam1 = exam_form.save()
                prescription = prescription_form.save(commit=False)
                prescription.prescriber_id = doctor.id
                prescription.save()
                occular = occular_form.save()

                exam1.prescription_id = prescription.id
                exam1.occular_exam_information_id = occular.id

                exam1.save()
                prescription.os_visual_acuity_distance = exam1.visual_accuity_aided_string_left_distance
                prescription.od_visual_acuity_distance = exam1.visual_accuity_aided_string_right_distance
                prescription.os_visual_acuity_near = exam1.visual_accuity_aided_string_left_near
                prescription.od_visual_acuity_near = exam1.visual_accuity_aided_string_right_near
                prescription.save()

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
                "date_of_birth": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=23 * 365)}",
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
                "effective_date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=5 * 365)}",
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
            emergency.patient_id = patient.id
            insurance.patient_id = patient.id
            emergency.save()
            insurance.save()
            exam_form = ExamCreationPostForm({
                "date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date()}",
                "time": f"{datetime.time(15, 30)}",
                "patient": patient,
                "doctor": doctor,
                "reason_for_visit": "Eyes be hurtin",
            })
            exam = exam_form.save(commit=False)
            exam.status = ExamModel.status_choices["progressing"]
            exam.save()
            for i in range(1, 6):
                exam_form = ExamCreationPostForm({
                    "date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=i * 30)}",
                    "time": f"{datetime.time(10, 30)}",
                    "arrival_time": f"{datetime.time(random.randint(9, 16), random.randint(1, 59))}",
                    "patient": patient,
                    "doctor": doctor,
                    "reason_for_visit": "Eyes be hurtin",
                })
                prescription_form = PrescriptionCreationForm({
                    "date_prescribed": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=i * 30)}",
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
                left_eye = open("test_data_images/test_left_eye.jpg", "rb")
                right_eye = open("test_data_images/test_right_eye.jpg", "rb")
                file_data = {
                    "image_of_left_eye": SimpleUploadedFile(
                        "test_data_images/test_left_eye.jpg", left_eye.read()
                    ),
                    "image_of_right_eye": SimpleUploadedFile(
                        "test_data_images/test_right_eye.jpg", right_eye.read()
                    ),
                }
                occular_form = OccularExamCreationForm(
                    {
                        "vitreous_segment": "CRITICAL",
                        "macula_segment": "CRITICAL",
                        "vasculature_segment": "CRITICAL",
                        "posterior_pole_segment": "CRITICAL",
                        "peripheral_retina_segment": "CRITICAL",
                        "misc_retina_segment": "CRITICAL",
                        "biabeti_eval_segment": "CRITICAL",
                        "htl_eval_segment": "CRITICAL",
                        "armd_segment": "CRITICAL",
                        "left_venous_pulsation": "+",
                        "right_venous_pulsation": "+",
                        "left_foveal_reflex": "+",
                        "right_venous_pulsation": "+",
                        "fundus_record": "Not Performed",
                        "dilated_with_drops": 1,
                        "dilated_with_drug": "Atropine",
                        "od_cup_ratio_horizontal": 0.01,
                        "od_cup_ratio_vertical": 0.01,
                        "os_cup_ratio_horizontal": 0.01,
                        "os_cup_ratio_vertical": 0.01,
                        "optic_nerve": "CRITICAL",
                        "nerve_fiber": "CRITICAL",
                    },
                    file_data,
                )
                aided_near = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="unaided_near")
                unaided_near = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="unaided_near")
                pinhole_aided_near = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_ph_near")
                pinhole_unaided_near = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_ph_near")
                aided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_distance")
                unaided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_near_distance")
                pinhole_aided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_ph_distance")
                pinhole_unaided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_ph_distance")
                exam1 = exam_form.save()
                prescription = prescription_form.save(commit=False)
                prescription.prescriber_id = doctor.id
                prescription.save()
                occular = occular_form.save()

                exam1.prescription_id = prescription.id
                exam1.occular_exam_information_id = occular.id
                exam1.occular_exam_information_id = occular.id
                aided_near = aided_near.save()
                unaided_near = unaided_near.save()
                pinhole_unaided_near = pinhole_unaided_near.save()
                pinhole_aided_near = pinhole_aided_near.save()
                aided_distance = aided_distance.save()
                unaided_distance = unaided_distance.save()
                pinhole_aided_distance = pinhole_aided_distance.save()
                pinhole_unaided_distance = pinhole_unaided_distance.save()

                exam1.visual_accuity_aided_near_id = aided_near.id
                exam1.visual_accuity_unaided_near_id = unaided_near.id
                exam1.visual_accuity_pinhole_unaided_near_id = pinhole_unaided_near.id
                exam1.visual_accuity_pinhole_aided_near_id = pinhole_aided_near.id
                exam1.visual_accuity_aided_distance_id = aided_distance.id
                exam1.visual_accuity_unaided_distance_id = unaided_distance.id
                exam1.visual_accuity_pinhole_aided_distance_id = pinhole_aided_distance.id
                exam1.visual_accuity_pinhole_unaided_distance_id = pinhole_unaided_distance.id

                exam1.save()
                prescription.os_visual_acuity_distance = exam1.visual_accuity_aided_string_left_distance
                prescription.od_visual_acuity_distance = exam1.visual_accuity_aided_string_right_distance
                prescription.os_visual_acuity_near = exam1.visual_accuity_aided_string_left_near
                prescription.od_visual_acuity_near = exam1.visual_accuity_aided_string_right_near
                prescription.save()

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
                "date_of_birth": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=23 * 365)}",
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
                "effective_date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=5 * 365)}",
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
            emergency.patient_id = patient.id
            insurance.patient_id = patient.id
            emergency.save()
            insurance.save()
            exam_form = ExamCreationPostForm({
                "date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date()}",
                "time": f"{datetime.time(10, 30)}",
                "patient": patient,
                "doctor": doctor,
                "reason_for_visit": "Eyes be hurtin",
            })
            exam = exam_form.save(commit=False)
            exam.status = ExamModel.status_choices['upcoming']
            exam.save()
            for i in range(1, 6):
                exam_form = ExamCreationPostForm({
                    "date": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=i * 30)}",
                    "time": f"{datetime.time(9, 30)}",
                    "arrival_time": f"{datetime.time(random.randint(9, 16), random.randint(1, 59))}",
                    "patient": patient,
                    "doctor": doctor,
                    "reason_for_visit": "Eyes be hurtin",
                })
                prescription_form = PrescriptionCreationForm({
                    "date_prescribed": f"{datetime.datetime.now(ZoneInfo("America/Indiana/Knox")).date() - datetime.timedelta(days=i * 30)}",
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
                left_eye = open("test_data_images/test_left_eye.jpg", "rb")
                right_eye = open("test_data_images/test_right_eye.jpg", "rb")
                file_data = {
                    "image_of_left_eye": SimpleUploadedFile(
                        "test_data_images/test_left_eye.jpg", left_eye.read()
                    ),
                    "image_of_right_eye": SimpleUploadedFile(
                        "test_data_images/test_right_eye.jpg", right_eye.read()
                    ),
                }
                occular_form = OccularExamCreationForm(
                    {
                        "vitreous_segment": "CRITICAL",
                        "macula_segment": "CRITICAL",
                        "vasculature_segment": "CRITICAL",
                        "posterior_pole_segment": "CRITICAL",
                        "peripheral_retina_segment": "CRITICAL",
                        "misc_retina_segment": "CRITICAL",
                        "biabeti_eval_segment": "CRITICAL",
                        "htl_eval_segment": "CRITICAL",
                        "armd_segment": "CRITICAL",
                        "left_venous_pulsation": "+",
                        "right_venous_pulsation": "+",
                        "left_foveal_reflex": "+",
                        "right_venous_pulsation": "+",
                        "fundus_record": "Not Performed",
                        "dilated_with_drops": 1,
                        "dilated_with_drug": "Atropine",
                        "od_cup_ratio_horizontal": 0.01,
                        "od_cup_ratio_vertical": 0.01,
                        "os_cup_ratio_horizontal": 0.01,
                        "os_cup_ratio_vertical": 0.01,
                        "optic_nerve": "CRITICAL",
                        "nerve_fiber": "CRITICAL",
                    },
                    file_data,
                )
                aided_near = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="unaided_near")
                unaided_near = VisualAccuitySubmissionForm({
                    "visual_acuity_measure_left": 10,
                    "visual_acuity_measure_right": 10,
                    "visual_acuity_measure_both": 10,
                }, prefix="unaided_near")
                pinhole_aided_near = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_ph_near")
                pinhole_unaided_near = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_ph_near")
                aided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_distance")
                unaided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_near_distance")
                pinhole_aided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="aided_ph_distance")
                pinhole_unaided_distance = VisualAccuitySubmissionForm({
                        "visual_acuity_measure_left": 10,
                        "visual_acuity_measure_right": 10,
                        "visual_acuity_measure_both": 10,
                    }, prefix="unaided_ph_distance")
                exam1 = exam_form.save()
                prescription = prescription_form.save(commit=False)
                prescription.prescriber_id = doctor.id
                prescription.save()
                occular = occular_form.save()

                exam1.prescription_id = prescription.id
                exam1.occular_exam_information_id = occular.id
                aided_near = aided_near.save()
                unaided_near = unaided_near.save()
                pinhole_unaided_near = pinhole_unaided_near.save()
                pinhole_aided_near = pinhole_aided_near.save()
                aided_distance = aided_distance.save()
                unaided_distance = unaided_distance.save()
                pinhole_aided_distance = pinhole_aided_distance.save()
                pinhole_unaided_distance = pinhole_unaided_distance.save()

                exam1.visual_accuity_aided_near_id = aided_near.id
                exam1.visual_accuity_unaided_near_id = unaided_near.id
                exam1.visual_accuity_pinhole_unaided_near_id = pinhole_unaided_near.id
                exam1.visual_accuity_pinhole_aided_near_id = pinhole_aided_near.id
                exam1.visual_accuity_aided_distance_id = aided_distance.id
                exam1.visual_accuity_unaided_distance_id = unaided_distance.id
                exam1.visual_accuity_pinhole_aided_distance_id = pinhole_aided_distance.id
                exam1.visual_accuity_pinhole_unaided_distance_id = pinhole_unaided_distance.id


                exam1.save()
                prescription.os_visual_acuity_distance = exam1.visual_accuity_aided_string_left_distance
                prescription.od_visual_acuity_distance = exam1.visual_accuity_aided_string_right_distance
                prescription.os_visual_acuity_near = exam1.visual_accuity_aided_string_left_near
                prescription.od_visual_acuity_near = exam1.visual_accuity_aided_string_right_near
                prescription.save()
