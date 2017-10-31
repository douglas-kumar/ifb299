# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fav', '0005_favorite_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='count',
        ),
    ]
