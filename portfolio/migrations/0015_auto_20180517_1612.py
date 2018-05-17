# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20180517_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='skill',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
