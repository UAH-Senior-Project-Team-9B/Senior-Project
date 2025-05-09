# Generated by Django 5.1.5 on 2025-04-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0040_exammodel_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualaccuitymodel',
            name='visual_acuity_measure_both',
            field=models.DecimalField(blank=True, choices=[('20/10', '20/10'), ('20/12.5', '20/12.5'), ('20/16', '20/16'), ('20/20', '20/20'), ('20/25', '20/25'), ('20/32', '20/32'), ('20/40', '20/40'), ('20/50', '20/50'), ('20/63', '20/63'), ('20/80', '20/80'), ('20/100', '20/100'), ('20/125', '20/125'), ('20/160', '20/160'), ('20/200', '20/200')], decimal_places=1, max_digits=4, null=True, verbose_name='OU Visual Accuity'),
        ),
        migrations.AlterField(
            model_name='visualaccuitymodel',
            name='visual_acuity_measure_left',
            field=models.DecimalField(blank=True, choices=[('20/10', '20/10'), ('20/12.5', '20/12.5'), ('20/16', '20/16'), ('20/20', '20/20'), ('20/25', '20/25'), ('20/32', '20/32'), ('20/40', '20/40'), ('20/50', '20/50'), ('20/63', '20/63'), ('20/80', '20/80'), ('20/100', '20/100'), ('20/125', '20/125'), ('20/160', '20/160'), ('20/200', '20/200')], decimal_places=1, max_digits=4, null=True, verbose_name='OS Visual Accuity'),
        ),
        migrations.AlterField(
            model_name='visualaccuitymodel',
            name='visual_acuity_measure_right',
            field=models.DecimalField(blank=True, choices=[('20/10', '20/10'), ('20/12.5', '20/12.5'), ('20/16', '20/16'), ('20/20', '20/20'), ('20/25', '20/25'), ('20/32', '20/32'), ('20/40', '20/40'), ('20/50', '20/50'), ('20/63', '20/63'), ('20/80', '20/80'), ('20/100', '20/100'), ('20/125', '20/125'), ('20/160', '20/160'), ('20/200', '20/200')], decimal_places=1, max_digits=4, null=True, verbose_name='OD Measurement'),
        ),
    ]
