# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_auto_20161004_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic_id', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('sentence', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic_id', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('sentence', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='summarizereview1',
            name='topic_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='summarizereview2',
            name='topic_id',
            field=models.IntegerField(null=True),
        ),
    ]
