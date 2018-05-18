# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_content_image_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image_media',
            field=models.ImageField(upload_to='images', null=True),
        ),
    ]
