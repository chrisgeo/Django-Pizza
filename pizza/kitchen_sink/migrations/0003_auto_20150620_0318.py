# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen_sink', '0002_auto_20150619_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='tpl',
            field=models.CharField(max_length=255, verbose_name=b'Template'),
        ),
    ]
