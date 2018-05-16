# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20180516_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill_item',
            name='perc_value',
            field=models.PositiveSmallIntegerField(default=50, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
