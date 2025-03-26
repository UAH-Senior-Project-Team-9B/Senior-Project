# Generated by Django 5.1.5 on 2025-03-25 05:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_remove_prescriptionmodel_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientusermodel',
            name='emergency_contact',
        ),
        migrations.AddField(
            model_name='exammodel',
            name='reason_for_visit',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientusermodel',
            name='phone_number',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Phone number must follow regulations', regex='^(?:[(][0-9]{3}[)][. -]|[(][0-9]{3}[)]|[0-9]{3}[. -])[0-9]{3}[ .-][0-9]{4}$')]),
        ),
        migrations.AlterField(
            model_name='patientusermodel',
            name='social_security_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='SSN must be in the format XXX-XX-XXXX', regex='^\\d{3}-\\d{2}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='patientusermodel',
            name='state',
            field=models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arisona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampsire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming'), ('Other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='patientusermodel',
            name='zip_code',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Zipcode must be in the format XXXXX or XXXXX-XXXX', regex='^\\d{5}-\\d{4}$|^\\d{5}$')]),
        ),
        migrations.CreateModel(
            name='EmergencyContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Dr.', 'Dr.'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], max_length=5)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_initial', models.CharField(blank=True, max_length=1)),
                ('last_name', models.CharField(max_length=30)),
                ('relationship', models.CharField(max_length=30)),
                ('phone_num', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.patientusermodel')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceProviderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=50)),
                ('contract_number', models.CharField(max_length=13)),
                ('group_number', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(4)])),
                ('effective_date', models.DateField()),
                ('co_pay', models.DecimalField(decimal_places=2, max_digits=255)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arisona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampsire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming'), ('Other', 'Other')], max_length=15)),
                ('zip_code', models.IntegerField()),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Phone number must follow regulations', regex='^(?:[(][0-9]{3}[)][. -]|[(][0-9]{3}[)]|[0-9]{3}[. -])[0-9]{3}[ .-][0-9]{4}$')])),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.patientusermodel')),
            ],
        ),
    ]
