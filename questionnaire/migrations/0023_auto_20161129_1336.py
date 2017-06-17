# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0022_auto_20161125_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire_exp3',
            name='q32_1',
            field=models.TextField(null=True, verbose_name=b'question32_1'),
        ),
        migrations.AddField(
            model_name='questionnaire_exp3',
            name='q32_2',
            field=models.TextField(null=True, verbose_name=b'question32_2'),
        ),
        migrations.AddField(
            model_name='questionnaire_exp3',
            name='q33_1',
            field=models.TextField(null=True, verbose_name=b'question33_1'),
        ),
        migrations.AddField(
            model_name='questionnaire_exp3',
            name='q33_2',
            field=models.TextField(null=True, verbose_name=b'question33_2'),
        ),
    ]
