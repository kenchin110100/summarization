# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0017_summarizereview_exp2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire_exp2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meta1', models.IntegerField(null=True, verbose_name=b'meta1')),
                ('meta2', models.DateTimeField(null=True, verbose_name=b'start_time')),
                ('meta3', models.DateTimeField(auto_now=True, verbose_name=b'end_time', null=True)),
                ('passwd', models.CharField(max_length=20, null=True)),
                ('user_name', models.CharField(max_length=20, null=True, verbose_name=b'question1')),
                ('q2', models.IntegerField(null=True, verbose_name=b'question2')),
                ('q3', models.IntegerField(null=True, verbose_name=b'question3')),
                ('q4', models.IntegerField(null=True, verbose_name=b'question4')),
                ('q5', models.IntegerField(null=True, verbose_name=b'question5')),
                ('q6', models.IntegerField(null=True, verbose_name=b'question6')),
                ('q7', models.IntegerField(null=True, verbose_name=b'question7')),
                ('q8', models.IntegerField(null=True, verbose_name=b'question8')),
                ('q9', models.IntegerField(null=True, verbose_name=b'question9')),
                ('q10', models.IntegerField(null=True, verbose_name=b'question10')),
                ('q11', models.IntegerField(null=True, verbose_name=b'question11')),
                ('q12', models.IntegerField(null=True, verbose_name=b'question12')),
                ('q13', models.IntegerField(null=True, verbose_name=b'question13')),
                ('q14', models.IntegerField(null=True, verbose_name=b'question14')),
                ('q15', models.IntegerField(null=True, verbose_name=b'question15')),
                ('q16', models.IntegerField(null=True, verbose_name=b'question16')),
                ('q17', models.IntegerField(null=True, verbose_name=b'question17')),
                ('q18', models.IntegerField(null=True, verbose_name=b'question18')),
                ('q19', models.IntegerField(null=True, verbose_name=b'question19')),
                ('q20', models.IntegerField(null=True, verbose_name=b'question20')),
                ('q21', models.IntegerField(null=True, verbose_name=b'question21')),
                ('q22', models.IntegerField(null=True, verbose_name=b'question22')),
                ('q23', models.IntegerField(null=True, verbose_name=b'question23')),
                ('q24', models.IntegerField(null=True, verbose_name=b'question24')),
                ('q25', models.IntegerField(null=True, verbose_name=b'question25')),
                ('q26', models.IntegerField(null=True, verbose_name=b'question26')),
                ('q27', models.IntegerField(null=True, verbose_name=b'question27')),
                ('q28', models.IntegerField(null=True, verbose_name=b'question28')),
                ('q29', models.IntegerField(null=True, verbose_name=b'question29')),
                ('q30', models.IntegerField(null=True, verbose_name=b'question30')),
                ('q31', models.IntegerField(null=True, verbose_name=b'question31')),
                ('q32', models.IntegerField(null=True, verbose_name=b'question32')),
                ('q33', models.IntegerField(null=True, verbose_name=b'question33')),
                ('q34', models.IntegerField(null=True, verbose_name=b'question34')),
                ('q35', models.IntegerField(null=True, verbose_name=b'question35')),
                ('q36_1', models.IntegerField(null=True, verbose_name=b'question36_1')),
                ('q36_2', models.TextField(null=True, verbose_name=b'question36_2')),
                ('q37_1', models.IntegerField(null=True, verbose_name=b'question37_1')),
                ('q37_2', models.TextField(null=True, verbose_name=b'question37_2')),
                ('q38_1', models.IntegerField(null=True, verbose_name=b'question38_1')),
                ('q38_2', models.TextField(null=True, verbose_name=b'question38_2')),
                ('q39_1', models.IntegerField(null=True, verbose_name=b'question39_1')),
                ('q39_2', models.TextField(null=True, verbose_name=b'question39_2')),
                ('q40', models.IntegerField(null=True, verbose_name=b'question40')),
                ('q41', models.IntegerField(null=True, verbose_name=b'question41')),
                ('q42_1', models.IntegerField(null=True, verbose_name=b'question42_1')),
                ('q42_2', models.IntegerField(null=True, verbose_name=b'question42_2')),
                ('q42_3', models.IntegerField(null=True, verbose_name=b'question42_3')),
            ],
        ),
    ]
