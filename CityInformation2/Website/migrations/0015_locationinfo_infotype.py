# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0014_auto_20171012_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationinfo',
            name='infoType',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
