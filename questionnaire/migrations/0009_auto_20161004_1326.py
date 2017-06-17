# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_summarizereview2'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarizereview1',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='summarizereview2',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
