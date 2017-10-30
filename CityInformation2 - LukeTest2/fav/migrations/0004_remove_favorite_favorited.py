# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fav', '0003_auto_20150914_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='favorited',
        ),
    ]
