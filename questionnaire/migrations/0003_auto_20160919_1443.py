# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_evaluation'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='img_eva1',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='img_eva2',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='img_eva3',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='img_eva4',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='img_eva5',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='img_eva6',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='img_eva7',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
