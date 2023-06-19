# Generated by Django 4.2 on 2023-06-11 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng', '0022_alter_dailystatus_date_alter_expenses_exdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystatus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 17, 55, 58, 794482)),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='exdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 17, 55, 58, 793484)),
        ),
        migrations.AlterField(
            model_name='mainamount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 17, 55, 58, 789482)),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 17, 55, 58, 790481)),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 17, 55, 58, 791481)),
        ),
        migrations.AlterField(
            model_name='salesdt',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 11, 17, 55, 58, 796481)),
        ),
    ]