# Generated by Django 2.2.3 on 2022-06-30 03:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 30, 3, 9, 34, 187919, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
