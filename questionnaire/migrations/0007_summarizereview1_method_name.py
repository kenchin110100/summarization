# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_summarizereview1'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarizereview1',
            name='method_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
