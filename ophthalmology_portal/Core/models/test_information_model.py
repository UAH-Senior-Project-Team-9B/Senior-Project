from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from django_cryptography.fields import encrypt

visual_acuity_choices = {
    "20/10": "20/10",
    "20/12.5": "20/12.5",
    "20/16": "20/16",
    "20/20": "20/20",
    "20/25": "20/25",
    "20/32": "20/32",
    "20/40": "20/40",
    "20/50": "20/50",
    "20/63": "20/63",
    "20/80": "20/80",
    "20/100": "20/100",
    "20/125": "20/125",
    "20/160": "20/160",
    "20/200": "20/200",
}

posterior_segment_choices = {
    "CRITICAL": "CRITICAL",
    "HIGH": "HIGH",
    "NORM": "NORM",
    "LOW": "LOW",
    "NOT CHECKED": "NOT CHECKED",
}

# Found using https://go.drugbank.com/categories/DBCAT000550
dilating_agents = {
    "Atropine": "Atropine",
    "Cyclopentolate": "Cyclopentolate",
    "Dipivefrin": "Dipivefrin",
    "Epinephrine": "Epinephrine",
    "Hydroxyamphetamine": "Hydroxyamphetamine",
    "Hyoscyamine": "Hyoscyamine",
    "Ibopamine": "Ibopamine",
    "Ketorolac": "Ketorolac",
    "Oxyphenonium": "Oxyphenonium",
    "Phenylephrine": "Phenylephrine",
    "Racepinephrine": "Racepinephrine",
    "Scopolamine": "Scopolamine",
    "Tropicamide": "Tropicamide",
    "Yohimbine": "Yohimbine",
}


class OccularExamModel(models.Model):
    vitreous_segment = encrypt(models.CharField(
        verbose_name="Vitreous Segment",
        choices=posterior_segment_choices,
        max_length=255,
    ))
    macula_segment = encrypt(models.CharField(
        verbose_name="Macula Segment", choices=posterior_segment_choices, max_length=255
    ))
    vasculature_segment = encrypt(models.CharField(
        verbose_name="Vasculature Segment",
        choices=posterior_segment_choices,
        max_length=255,
    ))
    posterior_pole_segment = encrypt(models.CharField(
        verbose_name="Posterior Pole Segment",
        choices=posterior_segment_choices,
        max_length=255,
    ))
    peripheral_retina_segment = encrypt(models.CharField(
        verbose_name="Peripheral Retina Segment",
        choices=posterior_segment_choices,
        max_length=255,
    ))
    misc_retina_segment = encrypt(models.CharField(
        verbose_name="Misc Retina Segment",
        choices=posterior_segment_choices,
        max_length=255,
    ))
    diabeti_eval_segment = encrypt(models.CharField(
        verbose_name="Diabeti Eval Segment",
        choices=posterior_segment_choices,
        max_length=255,
    ))
    htn_eval_segment = encrypt(models.CharField(
        verbose_name="HTL Evaluation Segment",
        choices=posterior_segment_choices,
        max_length=255,
    ))
    armd_segment = encrypt(models.CharField(
        verbose_name="ARMD Segment", choices=posterior_segment_choices, max_length=255
    ))

    # Ophthalmic Indicators
    left_venous_pulsation = encrypt(models.CharField(
        verbose_name="OS Sponeaneous Venous Pulsation",
        choices={"+": "+", "-": "-", "X": "X"},
        max_length=1,
    ))
    right_venous_pulsation = encrypt(models.CharField(
        verbose_name="OD Venous Pulsation",
        choices={"+": "+", "-": "-", "X": "X"},
        max_length=1,
    ))
    left_foveal_reflex = encrypt(models.CharField(
        verbose_name="OS Reflex", choices={"+": "+", "-": "-", "X": "X"}, max_length=1
    ))
    right_foveal_reflex = encrypt(models.CharField(
        verbose_name="OD Reflex", choices={"+": "+", "-": "-", "X": "X"}, max_length=1
    ))

    # Fundus Evaluation
    fundus_record = encrypt(models.CharField(
        verbose_name="Evaluation Performed",
        choices={
            "Not Performed": "Not Performed",
            "Small Pupil BIO": "Small Pupil BIO",
            "Dilated Eval": "Dilated Eval",
            "Undilated Eval": "Undilated Eval",
            "Optomap Imaging": "Optomap Imaging",
            "DFE with Optomap": "DFE with Optomap",
        },
        max_length=255,
    ))
    dilated_with_drops = encrypt(models.IntegerField(
        choices={
            1: "1 gtt",
            2: "2 gtt",
        }
    ))
    dilated_with_drug = encrypt(models.CharField(choices=dilating_agents, max_length=255))

    # Evaluated with
    d78_lens = encrypt(models.BooleanField(verbose_name="78D Lens"))
    d90_lens = encrypt(models.BooleanField(verbose_name="90D Lens"))
    d20_lens = encrypt(models.BooleanField(verbose_name="20D BIO Lens"))
    PR22_lens = encrypt(models.BooleanField(verbose_name="PR 2.2 BIO Lens"))
    scleral_depression = encrypt(models.BooleanField(verbose_name="Scleral Depression"))
    ophthalmoscope = encrypt(models.BooleanField(verbose_name="Direct Opthalmoscope"))
    other = encrypt(models.BooleanField(verbose_name="Other"))
    other_information = encrypt(models.TextField(max_length=255, null=True, blank=True))

    # Notes
    advised = encrypt(models.BooleanField(verbose_name="Patient Advised of effects of DFE"))
    rescheduled = encrypt(models.BooleanField(verbose_name="DFE to be Rescheduled"))
    declined = encrypt(models.BooleanField(verbose_name="DFE Declined"))
    imaging = encrypt(models.BooleanField(verbose_name="Fundus Imaging Performed"))
    refused = encrypt(models.BooleanField(verbose_name="DFE refused AME"))
    not_indicated = encrypt(models.BooleanField(verbose_name="DFE Not Indicated"))
    contraindicated = encrypt(models.BooleanField(verbose_name="DFE Contraindicated"))
    recent = encrypt(models.BooleanField(verbose_name="Recent DFE"))

    od_cup_ratio_horizontal = encrypt(models.DecimalField(
        verbose_name="OD Cup-Disc Horizontal Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    ))
    od_cup_ratio_vertical = encrypt(models.DecimalField(
        verbose_name="OD Cup-Disc Vertical Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    ))
    os_cup_ratio_horizontal = encrypt(models.DecimalField(
        verbose_name="OS Cup-Disc Horizontal Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    ))
    os_cup_ratio_vertical = encrypt(models.DecimalField(
        verbose_name="OS Cup-Disc Vertical Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    ))

    # Optic Nerve Head Assesment (May need revisit based on Optic Nerve Descriptors definition)
    optic_nerve = encrypt(models.CharField(
        verbose_name="Optic Nerve", choices=posterior_segment_choices, max_length=255
    ))
    nerve_fiber = encrypt(models.CharField(
        verbose_name="Nerve Fiber Layer",
        choices=posterior_segment_choices,
        max_length=255,
    ))

    od_deep = encrypt(models.BooleanField(verbose_name="OD Deep/Lamina"))
    od_shallow = encrypt(models.BooleanField(verbose_name="OD Shallow"))
    od_round = encrypt(models.BooleanField(verbose_name="OD Round"))
    od_oval = encrypt(models.BooleanField(verbose_name="OD Oval"))
    od_temp = encrypt(models.BooleanField(verbose_name="OD Temp. sloping"))
    od_under = encrypt(models.BooleanField(verbose_name="OD undermining"))
    od_atrophy = encrypt(models.BooleanField(verbose_name="OD Peripap Atrophy"))
    od_scleral = encrypt(models.BooleanField(verbose_name="OD Scleral Crescent"))
    od_pigment = encrypt(models.BooleanField(verbose_name="OD Pigment Crescent"))
    od_pit = encrypt(models.BooleanField(verbose_name="OD Optic Pit"))
    od_muyelination = encrypt(models.BooleanField(verbose_name="OD Muyelination"))
    od_remnants = encrypt(models.BooleanField(verbose_name="OD Glial Remnants"))

    os_deep = encrypt(models.BooleanField(verbose_name="OS Deep/Lamina"))
    os_shallow = encrypt(models.BooleanField(verbose_name="OS Shallow"))
    os_round = encrypt(models.BooleanField(verbose_name="OS Round"))
    os_oval = encrypt(models.BooleanField(verbose_name="OS Oval"))
    os_temp = encrypt(models.BooleanField(verbose_name="OS Temp. sloping"))
    os_under = encrypt(models.BooleanField(verbose_name="OS undermining"))
    os_atrophy = encrypt(models.BooleanField(verbose_name="OS Peripap Atrophy"))
    os_scleral = encrypt(models.BooleanField(verbose_name="OS Scleral Crescent"))
    os_pigment = encrypt(models.BooleanField(verbose_name="OS Pigment Crescent"))
    os_pit = encrypt(models.BooleanField(verbose_name="OS Optic Pit"))
    os_muyelination = encrypt(models.BooleanField(verbose_name="OS Muyelination"))
    os_remnants = encrypt(models.BooleanField(verbose_name="OS Glial Remnants"))

    image_of_left_eye = encrypt(models.ImageField(upload_to="left_eye/"))
    image_of_right_eye = encrypt(models.ImageField(upload_to="right_eye/"))

    class Meta:
        permissions = [
            ("patient", "Patient Permissions"),
            ("doctor", "Doctor Permissions"),
            ("manager", "Manager Permissions"),
        ]


class VisualAccuityModel(models.Model):
    visual_acuity_measure_left = encrypt(models.CharField(
        verbose_name="OS Visual Accuity",
        choices=visual_acuity_choices,
        max_length=255,
        blank=True,
        null=True,
    ))
    visual_acuity_measure_right = encrypt(models.CharField(
        verbose_name="OD Measurement",
        choices=visual_acuity_choices,
        max_length=255,
        blank=True,
        null=True,
    ))
    visual_acuity_measure_both = encrypt(models.CharField(
        verbose_name="OU Visual Accuity",
        choices=visual_acuity_choices,
        max_length=255,
        blank=True,
        null=True,
    ))

    class Meta:
        permissions = [
            ("patient", "Patient Permissions"),
            ("doctor", "Doctor Permissions"),
            ("manager", "Manager Permissions"),
        ]
