# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_skill_skill_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill_item',
            name='perc_value',
            field=models.IntegerField(default=50),
        ),
    ]
