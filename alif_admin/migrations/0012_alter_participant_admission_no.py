# Generated by Django 5.1.3 on 2024-11-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alif_admin', '0011_alter_participant_student_cls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='admission_no',
            field=models.CharField(max_length=20),
        ),
    ]
