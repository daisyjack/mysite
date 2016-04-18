# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.CharField(default=186, max_length=40),
            preserve_default=False,
        ),
    ]
