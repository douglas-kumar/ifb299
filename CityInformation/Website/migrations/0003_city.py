# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_college_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=60)),
            ],
        ),
    ]
