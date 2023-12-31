# Generated by Django 4.2 on 2023-05-25 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng', '0010_alter_expenses_exdate_alter_mainamount_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='expstatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='exdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 25, 13, 23, 29, 854523)),
        ),
        migrations.AlterField(
            model_name='mainamount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 25, 13, 23, 29, 851524)),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 25, 13, 23, 29, 852526)),
        ),
    ]
