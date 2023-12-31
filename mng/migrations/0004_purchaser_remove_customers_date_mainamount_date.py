# Generated by Django 4.1.7 on 2023-04-26 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mng", "0003_mainamount_customers_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="purchaser",
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
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 4, 26, 12, 38, 24, 828440)
                    ),
                ),
                ("seller_name", models.CharField(max_length=100)),
                ("product_name", models.CharField(max_length=100)),
                ("rate", models.IntegerField(default=0)),
                ("weight", models.CharField(max_length=100)),
                ("amount", models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name="customers",
            name="date",
        ),
        migrations.AddField(
            model_name="mainamount",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 26, 12, 38, 24, 828440)
            ),
        ),
    ]
