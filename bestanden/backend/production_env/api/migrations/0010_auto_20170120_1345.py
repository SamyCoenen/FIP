# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20170119_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculationparameter',
            name='tech_budget',
            field=models.IntegerField(default=400),
        ),
        migrations.AlterField(
            model_name='taxscale',
            name='bruto',
            field=models.IntegerField(),
        ),
    ]
