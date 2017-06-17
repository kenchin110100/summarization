# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0021_questionnaire_exp3'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarizereview_exp2',
            name='eva7',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='summarizereview_exp2',
            name='review',
            field=models.TextField(null=True),
        ),
    ]
