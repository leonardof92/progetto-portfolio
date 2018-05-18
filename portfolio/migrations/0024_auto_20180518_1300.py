# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_auto_20180518_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to='images', blank=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to='images', blank=True),
        ),
    ]
