# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20180517_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image_media',
            field=models.ImageField(upload_to='portfolio/media', null=True),
        ),
    ]
