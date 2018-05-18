# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_auto_20180518_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(upload_to='images', null=True),
        ),
    ]
