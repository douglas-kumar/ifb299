# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0007_event_publictrans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=60),
        ),
        migrations.AlterField(
            model_name='city',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=60),
        ),
    ]
