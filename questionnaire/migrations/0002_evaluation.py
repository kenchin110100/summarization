# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hotel_name', models.CharField(max_length=20, null=True)),
                ('eva1', models.DecimalField(null=True, max_digits=3, decimal_places=2)),
                ('eva2', models.DecimalField(null=True, max_digits=3, decimal_places=2)),
                ('eva3', models.DecimalField(null=True, max_digits=3, decimal_places=2)),
                ('eva4', models.DecimalField(null=True, max_digits=3, decimal_places=2)),
                ('eva5', models.DecimalField(null=True, max_digits=3, decimal_places=2)),
                ('eva6', models.DecimalField(null=True, max_digits=3, decimal_places=2)),
                ('eva7', models.DecimalField(null=True, max_digits=3, decimal_places=2)),
            ],
        ),
    ]
