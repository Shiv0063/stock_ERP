# Generated by Django 4.2 on 2023-05-31 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng', '0016_stock_amount_alter_dailystatus_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailystatus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 12, 59, 17, 342757)),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='exdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 12, 59, 17, 341757)),
        ),
        migrations.AlterField(
            model_name='mainamount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 12, 59, 17, 338758)),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 12, 59, 17, 339759)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 12, 59, 17, 340758)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
