# Generated by Django 5.1.3 on 2024-11-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alif_admin', '0005_participant_category_alter_participant_added_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='code_letter',
            field=models.CharField(default='', max_length=20),
        ),
    ]
