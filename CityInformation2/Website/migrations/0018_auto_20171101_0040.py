# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0017_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website.LocationInfo'),
        ),
    ]
