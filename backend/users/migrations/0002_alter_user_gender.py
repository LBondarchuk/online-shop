# Generated by Django 4.2.5 on 2023-11-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "Male"), ("Female", "Female")],
                max_length=50,
            ),
        ),
    ]