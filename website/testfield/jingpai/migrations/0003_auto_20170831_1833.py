# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jingpai', '0002_auto_20170831_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_des',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='des',
            field=models.TextField(default=datetime.date(2017, 8, 31)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.ImageField(null=True, upload_to=b'phots/', blank=True),
            preserve_default=True,
        ),
    ]
