# Generated by Django 4.1.7 on 2023-04-26 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mng", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="mainamount",
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
                ("amount", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="customers",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 26, 12, 12, 34, 441058)
            ),
        ),
    ]
