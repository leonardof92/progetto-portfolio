# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20180516_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='content',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
