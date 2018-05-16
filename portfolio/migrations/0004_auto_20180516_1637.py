# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_skill_item_perc_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill_item',
            name='perc_value',
            field=models.PositiveSmallIntegerField(max_length=100, default=50),
        ),
    ]
