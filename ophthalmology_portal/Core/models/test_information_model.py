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
        name="Vitreous Segment", choices=posterior_segment_choices, max_length=255
    )
    macula_segment = models.CharField(
        name="Macula Segment", choices=posterior_segment_choices, max_length=255
    )
    vasculature_segment = models.CharField(
        name="Vasculature Segment", choices=posterior_segment_choices, max_length=255
    )
    posterior_pole_segment = models.CharField(
        name="Posterior Pole Segment", choices=posterior_segment_choices, max_length=255
    )
    peripheral_retina_segment = models.CharField(
        name="Peripheral Retina Segment",
        choices=posterior_segment_choices,
        max_length=255,
    )
    misc_retina_segment = models.CharField(
        name="Misc Retina Segment", choices=posterior_segment_choices, max_length=255
    )
    biabeti_eval_segment = models.CharField(
        name="Diabeti Eval Segment", choices=posterior_segment_choices, max_length=255
    )
    htl_eval_segment = models.CharField(
        name="HTL Evaluation Segment", choices=posterior_segment_choices, max_length=255
    )
    armd_segment = models.CharField(
        name="ARMD Segment", choices=posterior_segment_choices, max_length=255
    )

    # Ophthalmic Indicators
    left_venous_pulsation = models.CharField(
        name="OS Sponeaneous Venous Pulsation",
        choices={"+": "+", "-": "-", "X": "X"},
        max_length=1,
    )
    right_venous_pulsation = models.CharField(
        name="OD Venous Pulsation", choices={"+": "+", "-": "-", "X": "X"}, max_length=1
    )
    left_foveal_reflex = models.CharField(
        name="OS Reflex", choices={"+": "+", "-": "-", "X": "X"}, max_length=1
    )
    right_venous_pulsation = models.CharField(
        name="OD Reflex", choices={"+": "+", "-": "-", "X": "X"}, max_length=1
    )

    # Fundus Evaluation
    fundus_record = models.CharField(
        name="Evaluation Performed",
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
    d78_lens = models.BooleanField(name="78D Lens")
    d90_lens = models.BooleanField(name="90D Lens")
    d20_lens = models.BooleanField(name="20D BIO Lens")
    PR22_lens = models.BooleanField(name="PR 2.2 BIO Lens")
    scleral_depression = models.BooleanField(name="Scleral Depression")
    ophthalmoscope = models.BooleanField(name="Direct Opthalmoscope")
    other = models.BooleanField(name="Other")
    other_information = models.TextField(max_length=255)

    # Notes
    advised = models.BooleanField(name="Patient Advised of effects of DFE")
    rescheduled = models.BooleanField(name="DFE to be Rescheduled")
    declined = models.BooleanField(name="DFE Declined")
    imaging = models.BooleanField(name="Fundus Imaging Performed")
    refused = models.BooleanField(name="DFE refused AME")
    not_indicated = models.BooleanField(name="DFE Not Indicated")
    contraindicated = models.BooleanField(name="DFE Contraindicated")
    recent = models.BooleanField(name="Recent DFE")

    od_cup_ratio_horizontal = models.DecimalField(
        name="OD Cup-Disc Horizontal Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    od_cup_ratio_vertical = models.DecimalField(
        name="OD Cup-Disc Vertical Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_cup_ratio_horizontal = models.DecimalField(
        name="OS Cup-Disc Horizontal Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )
    os_cup_ratio_vertical = models.DecimalField(
        name="OS Cup-Disc Vertical Ratio",
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        max_digits=3,
    )

    # Optic Nerve Head Assesment (May need revisit based on Optic Nerve Descriptors definition)
    optic_nerve = models.CharField(
        name="Optic Nerve", choices=posterior_segment_choices, max_length=255
    )
    nerve_fiber = models.CharField(
        name="Nerve Fiber Layer", choices=posterior_segment_choices, max_length=255
    )

    od_deep = models.BooleanField(name="OD Deep/Lamina")
    od_shallow = models.BooleanField(name="OD Shallow")
    od_round = models.BooleanField(name="OD Round")
    od_oval = models.BooleanField(name="OD Oval")
    od_temp = models.BooleanField(name="OD Temp. sloping")
    od_under = models.BooleanField(name="OD undermining")
    od_atrophy = models.BooleanField(name="OD Peripap Atrophy")
    od_scleral = models.BooleanField(name="OD Scleral Crescent")
    od_pigment = models.BooleanField(name="OD Pigment Crescent")
    od_pit = models.BooleanField(name="OD Optic Pit")
    od_muyelination = models.BooleanField(name="OD Muyelination")
    od_remnants = models.BooleanField(name="OD Glial Remnants")

    os_deep = models.BooleanField(name="OS Deep/Lamina")
    os_shallow = models.BooleanField(name="OS Shallow")
    os_round = models.BooleanField(name="OS Round")
    os_oval = models.BooleanField(name="OS Oval")
    os_temp = models.BooleanField(name="OS Temp. sloping")
    os_under = models.BooleanField(name="OS undermining")
    os_atrophy = models.BooleanField(name="OS Peripap Atrophy")
    os_scleral = models.BooleanField(name="OS Scleral Crescent")
    os_pigment = models.BooleanField(name="OS Pigment Crescent")
    os_pit = models.BooleanField(name="OS Optic Pit")
    os_muyelination = models.BooleanField(name="OS Muyelination")
    os_remnants = models.BooleanField(name="OS Glial Remnants")

    class Meta:
        permissions = [
            ("patient", "Patient Permissions"),
            ("doctor", "Doctor Permissions"),
            ("manager", "Manager Permissions"),
        ]


class VisualAccuityModel(models.Model):
    distance = models.CharField(choices={"D": "D", "N": "N"}, max_length=255)

    visual_acuity_measure_left = models.DecimalField(
        name="OS Visual Accuity",
        choices=visual_acuity_choices,
        max_digits=4,
        decimal_places=1,
    )
    corrector_indicator_left = models.CharField(
        name="Corrector Indicator",
        choices={"cc": "cc (with)", "sc": "sc (without)"},
        max_length=255,
    )
    pinhole_left = models.BooleanField(
        name="OS Pinhole Occluder"
    )  # Needs to be displayed as "PH" when viewing completed data

    visual_acuity_measure_right = models.DecimalField(
        name="Right Eye Measurement",
        choices=visual_acuity_choices,
        max_digits=4,
        decimal_places=1,
    )
    corrector_indicator_right = models.CharField(
        name="OD Corrector Indicator",
        choices={"cc": "cc (with)", "sc": "sc (without)"},
        max_length=255,
    )
    pinhole_right = models.BooleanField(name="OD Pinhole Occluder")

    visual_acuity_measure_both = models.DecimalField(
        name="OU Visual Accuity",
        choices=visual_acuity_choices,
        max_digits=4,
        decimal_places=1,
    )
    corrector_indicator_both = models.CharField(
        name="OU Corrector Indicator",
        choices={"cc": "cc (with)", "sc": "sc (without)"},
        max_length=255,
    )
    pinhole_both = models.BooleanField(name="OU Pinhole Occluder")

    def distance_measurement(self):
        if self.distance == "D":
            return "20 feet/6.1 meters"
        else:
            return "15.7 inches/40 centimeters"

    class Meta:
        permissions = [
            ("patient", "Patient Permissions"),
            ("doctor", "Doctor Permissions"),
            ("manager", "Manager Permissions"),
        ]
