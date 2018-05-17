# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20180517_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='image',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.CharField(null=True, max_length=200),
        ),
    ]
