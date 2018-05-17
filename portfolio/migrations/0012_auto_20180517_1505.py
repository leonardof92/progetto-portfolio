# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20180517_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
