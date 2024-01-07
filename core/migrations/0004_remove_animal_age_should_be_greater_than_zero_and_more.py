# Generated by Django 4.2.5 on 2024-01-07 05:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_animal_age_should_be_greater_than_zero_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="animal",
            name="age_should_be_greater_than_zero",
        ),
        migrations.AlterField(
            model_name="animal",
            name="age",
            field=models.FloatField(
                help_text="Age of animal in years",
                validators=[django.core.validators.MinValueValidator(0.0)],
            ),
        ),
    ]
