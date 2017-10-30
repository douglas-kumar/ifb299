# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fav', '0011_favorite_cookie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='cookie',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
