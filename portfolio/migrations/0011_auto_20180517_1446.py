# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20180517_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
