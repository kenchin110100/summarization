# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0019_auto_20161107_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire_exp2',
            name='meta3',
            field=models.DateTimeField(null=True, verbose_name=b'end_time'),
        ),
    ]
