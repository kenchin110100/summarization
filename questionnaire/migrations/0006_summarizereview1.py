# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_review2'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummarizeReview1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_id', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('sentence', models.TextField(null=True)),
            ],
        ),
    ]
