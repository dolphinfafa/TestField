# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jingpai', '0003_auto_20170831_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(null=True, upload_to=b'photos/', blank=True),
        ),
    ]
