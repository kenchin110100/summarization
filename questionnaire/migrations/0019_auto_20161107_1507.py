# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0018_questionnaire_exp2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaire_exp2',
            old_name='user_name',
            new_name='q1',
        ),
    ]
