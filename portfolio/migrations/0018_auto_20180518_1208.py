# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20180518_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image_media',
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='images', null=True),
        ),
    ]
