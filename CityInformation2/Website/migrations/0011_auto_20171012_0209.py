# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-11 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0010_auto_20171006_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='locationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=250, null=True)),
                ('image', models.CharField(max_length=1000)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('industryType', models.CharField(blank=True, max_length=500, null=True)),
                ('departments', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='college',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='Industries',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.DeleteModel(
            name='Mall',
        ),
        migrations.DeleteModel(
            name='Museum',
        ),
        migrations.DeleteModel(
            name='Park',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.DeleteModel(
            name='Zoo',
        ),
    ]