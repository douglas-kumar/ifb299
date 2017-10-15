# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-12 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0013_auto_20171012_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.City'),
        ),
        migrations.AddField(
            model_name='locationinfo',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.City'),
        ),
        migrations.AddField(
            model_name='publictrans',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.City'),
        ),
    ]