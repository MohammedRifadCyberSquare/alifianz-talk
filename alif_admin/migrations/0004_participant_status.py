# Generated by Django 5.1.3 on 2024-11-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alif_admin', '0003_remove_participant_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='status',
            field=models.CharField(default='active', max_length=100),
        ),
    ]
