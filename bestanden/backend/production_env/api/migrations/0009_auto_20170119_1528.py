# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170119_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxscale',
            name='year',
            field=models.IntegerField(default=2016),
        ),
    ]
