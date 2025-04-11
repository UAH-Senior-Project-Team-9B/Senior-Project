from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

visual_acuity_choices = {
    10: "20/10",
    12.5: "20/12.5",
    16: "20/16",
    20: "20/20",
    25: "20/25",
    32: "20/32",
    40: "20/40",
    50: "20/50",
    63: "20/63",
    80: "20/80",
    100: "20/100",
    125: "20/125",
    160: "20/160",
    200: "20/200",
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
    vitreous_segment = models.CharField(
        verbose_name="Vitreous Segment", choices=posterior_segment_choices, max_length=255
    )
    macula_segment = models.CharField(
        verbose_name="Macula Segment", choices=posterior_segment_choices, max_length=255
    )
    vasculature_segment = models.CharField(
        verbose_name="Vasculature Segment", choices=posterior_segment_choices, max_length=255
    )
    posterior_pole_segment = models.CharField(
        verbose_name="Posterior Pole Segment", choices=posterior_segment_choices, max_length=255
    )
    peripheral_retina_segment = models.CharField(
        verbose_name="Peripheral Retina Segment",
        choices=posterior_segment_choices,
        max_length=255,
    )
    misc_retina_segment = models.CharField(
        verbose_name="Misc Retina Segment", choices=posterior_segment_choices, max_length=255
    )
    diabeti_eval_segment = models.CharField(
        verbose_name="Diabeti Eval Segment", choices=posterior_segment_choices, max_length=255
    )
    htn_eval_segment = models.CharField(
        verbose_name="HTL Evaluation Segment", choices=posterior_segment_choices, max_length=255
    )
    armd_segment = models.CharField(
        verbose_name="ARMD Segment", choices=posterior_segment_choices, max_length=255
    )

    # Ophthalmic Indicators
    left_venous_pulsation = models.CharField(
        verbose_name="OS Sponeaneous Venous Pulsation",
        choices={"+": "+", "-": "-", "X": "X"},
        max_length=1,
    )
    right_venous_pulsation = models.CharField(
        verbose_name="OD Venous Pulsation", choices={"+": "+", "-": "-", "X": "X"}, max_length=1
    )
    left_foveal_reflex = models.CharField(
        verbose_name="OS Reflex", choices={"+": "+", "-": "-", "X": "X"}, max_length=1
    )
    right_venous_pulsation = models.CharField(
        verbose_name="OD Reflex", choices={"+": "+", "-": "-", "X": "X"}, max_length=1
    )

    # Fundus Evaluation
    fundus_record = models.CharField(
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
    )
    dilated_with_drops = models.IntegerField(
        choices={
            1: "1 gtt",
            2: "2 gtt",
        }
    )
    dilated_with_drug = models.CharField(choices=dilating_agents, max_length=255)

    # Evaluated with
    d78_lens = models.BooleanField(verbose_name="78D Lens")
    d90_lens = models.BooleanField(verbose_name="90D Lens")
    d20_lens = models.BooleanField(verbose_name="20D BIO Lens")
    PR22_lens = models.BooleanField(verbose_name="PR 2.2 BIO Lens")
    scleral_depression = models.BooleanField(verbose_name="Scleral Depression")
    ophthalmoscope = models.BooleanField(verbose_name="Direct Opthalmoscope")
    other = models.BooleanField(verbose_name="Other")
    other_information = models.TextField(max_length=255, null=True, blank=True)

    # Notes
    advised = models.BooleanField(verbose_name="Patient Advised of effects of DFE")
    rescheduled = models.BooleanField(verbose_name="DFE to be Rescheduled")
    declined = models.BooleanField(verbose_name="DFE Declined")
    imaging = models.BooleanField(verbose_name="Fundus Imaging Performed")
    refused = models.BooleanField(verbose_name="DFE refused AME")
    not_indicated = models.BooleanField(verbose_name="DFE Not Indicated")
    contraindicated = models.BooleanField(verbose_name="DFE Contraindicated")
    recent = models.BooleanField(verbose_name="Recent DFE")

    od_cup_ratio_horizontal = models.DecimalField(
        verbose_name="OD Cup-Disc Horizontal Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    od_cup_ratio_vertical = models.DecimalField(
        verbose_name="OD Cup-Disc Vertical Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_cup_ratio_horizontal = models.DecimalField(
        verbose_name="OS Cup-Disc Horizontal Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_cup_ratio_vertical = models.DecimalField(
        verbose_name="OS Cup-Disc Vertical Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )

    # Optic Nerve Head Assesment (May need revisit based on Optic Nerve Descriptors definition)
    optic_nerve = models.CharField(
        verbose_name="Optic Nerve", choices=posterior_segment_choices, max_length=255
    )
    nerve_fiber = models.CharField(
        verbose_name="Nerve Fiber Layer", choices=posterior_segment_choices, max_length=255
    )

    od_deep = models.BooleanField(verbose_name="OD Deep/Lamina")
    od_shallow = models.BooleanField(verbose_name="OD Shallow")
    od_round = models.BooleanField(verbose_name="OD Round")
    od_oval = models.BooleanField(verbose_name="OD Oval")
    od_temp = models.BooleanField(verbose_name="OD Temp. sloping")
    od_under = models.BooleanField(verbose_name="OD undermining")
    od_atrophy = models.BooleanField(verbose_name="OD Peripap Atrophy")
    od_scleral = models.BooleanField(verbose_name="OD Scleral Crescent")
    od_pigment = models.BooleanField(verbose_name="OD Pigment Crescent")
    od_pit = models.BooleanField(verbose_name="OD Optic Pit")
    od_muyelination = models.BooleanField(verbose_name="OD Muyelination")
    od_remnants = models.BooleanField(verbose_name="OD Glial Remnants")

    os_deep = models.BooleanField(verbose_name="OS Deep/Lamina")
    os_shallow = models.BooleanField(verbose_name="OS Shallow")
    os_round = models.BooleanField(verbose_name="OS Round")
    os_oval = models.BooleanField(verbose_name="OS Oval")
    os_temp = models.BooleanField(verbose_name="OS Temp. sloping")
    os_under = models.BooleanField(verbose_name="OS undermining")
    os_atrophy = models.BooleanField(verbose_name="OS Peripap Atrophy")
    os_scleral = models.BooleanField(verbose_name="OS Scleral Crescent")
    os_pigment = models.BooleanField(verbose_name="OS Pigment Crescent")
    os_pit = models.BooleanField(verbose_name="OS Optic Pit")
    os_muyelination = models.BooleanField(verbose_name="OS Muyelination")
    os_remnants = models.BooleanField(verbose_name="OS Glial Remnants")

    image_of_left_eye = models.ImageField(upload_to="database/left_eye/")
    image_of_right_eye = models.ImageField(upload_to="database/right_eye/")

    class Meta:
        permissions = [
            ("patient", "Patient Permissions"),
            ("doctor", "Doctor Permissions"),
            ("manager", "Manager Permissions"),
        ]


class VisualAccuityModel(models.Model):

    visual_acuity_measure_left = models.DecimalField(
        verbose_name="OS Visual Accuity",
        choices=visual_acuity_choices,
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True
    )
    visual_acuity_measure_right = models.DecimalField(
        verbose_name="OD Measurement",
        choices=visual_acuity_choices,
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True
    )
    visual_acuity_measure_both = models.DecimalField(
        verbose_name="OU Visual Accuity",
        choices=visual_acuity_choices,
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True
    )


    class Meta:
        permissions = [
            ("patient", "Patient Permissions"),
            ("doctor", "Doctor Permissions"),
            ("manager", "Manager Permissions"),
        ]
