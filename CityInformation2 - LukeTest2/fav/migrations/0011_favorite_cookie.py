# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fav', '0010_remove_favorite_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='cookie',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
