# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0009_auto_20161004_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicsummarize',
            old_name='sentence',
            new_name='word1',
        ),
        migrations.RemoveField(
            model_name='topicsummarize',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='topicsummarize',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='topicsummarize',
            name='user_name',
        ),
        migrations.AddField(
            model_name='topicsummarize',
            name='word2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='topicsummarize',
            name='word3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='topicsummarize',
            name='word4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='topicsummarize',
            name='word5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='topicsummarize',
            name='word6',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='topicsummarize',
            name='word7',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='topicsummarize',
            name='word8',
            field=models.TextField(null=True),
        ),
    ]
