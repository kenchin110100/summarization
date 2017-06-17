# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0015_auto_20161013_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('review', models.TextField(null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('eva1', models.IntegerField(null=True)),
                ('eva2', models.IntegerField(null=True)),
                ('eva3', models.IntegerField(null=True)),
                ('eva4', models.IntegerField(null=True)),
                ('eva5', models.IntegerField(null=True)),
                ('eva6', models.IntegerField(null=True)),
                ('eva7', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('review', models.TextField(null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('eva1', models.IntegerField(null=True)),
                ('eva2', models.IntegerField(null=True)),
                ('eva3', models.IntegerField(null=True)),
                ('eva4', models.IntegerField(null=True)),
                ('eva5', models.IntegerField(null=True)),
                ('eva6', models.IntegerField(null=True)),
                ('eva7', models.IntegerField(null=True)),
            ],
        ),
    ]
