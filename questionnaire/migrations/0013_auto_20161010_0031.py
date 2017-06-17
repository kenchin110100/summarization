# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0012_questionnaire1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire1',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]
