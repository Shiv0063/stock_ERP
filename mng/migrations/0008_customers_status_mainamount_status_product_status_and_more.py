# Generated by Django 4.2 on 2023-05-24 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng', '0007_purchaser_bkamount_alter_mainamount_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mainamount',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchaser',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mainamount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 19, 36, 19, 932414)),
        ),
        migrations.AlterField(
            model_name='purchaser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 19, 36, 19, 933412)),
        ),
    ]