# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_calculationparameter_vaa_laptop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculationparameter',
            name='vaa_smartphone',
            field=models.FloatField(default=12.5),
        ),
    ]
