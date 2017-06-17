# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20160919_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicSummarize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic_id', models.IntegerField(null=True)),
                ('rank', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('sentence', models.TextField(null=True)),
                ('date_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
