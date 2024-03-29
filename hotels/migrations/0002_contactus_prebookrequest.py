# Generated by Django 5.0 on 2024-02-11 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hotels", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sender_name", models.CharField(max_length=100)),
                ("sender_email", models.CharField(max_length=80)),
                ("contact_subject", models.CharField(max_length=150)),
                ("contact_message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PreBookRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("requester_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=80)),
                ("check_in", models.DateField()),
                ("check_out", models.DateField()),
                ("adult", models.CharField(max_length=80)),
                ("child", models.CharField(max_length=80)),
                ("special_req", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotels.hotel"
                    ),
                ),
            ],
        ),
    ]
