# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0016_review3_review4'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummarizeReview_exp2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_id', models.IntegerField(null=True)),
                ('topic_id', models.IntegerField(null=True)),
                ('hotel_name', models.CharField(max_length=20, null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('sentence', models.TextField(null=True)),
                ('method_name', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
