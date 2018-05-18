# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20180518_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(null='images/None/no-img.jpg', upload_to='images'),
        ),
    ]
