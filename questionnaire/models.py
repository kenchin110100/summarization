# coding: utf-8
from django.db import models
from datetime import datetime

# Create your models here.


class Review1(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=20, null=True)
    review = models.TextField(null=True)
    date_time = models.DateTimeField(null=True)
    eva1 = models.IntegerField(null=True)
    eva2 = models.IntegerField(null=True)
    eva3 = models.IntegerField(null=True)
    eva4 = models.IntegerField(null=True)
    eva5 = models.IntegerField(null=True)
    eva6 = models.IntegerField(null=True)
    eva7 = models.IntegerField(null=True)


class Review2(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=20, null=True)
    review = models.TextField(null=True)
    date_time = models.DateTimeField(null=True)
    eva1 = models.IntegerField(null=True)
    eva2 = models.IntegerField(null=True)
    eva3 = models.IntegerField(null=True)
    eva4 = models.IntegerField(null=True)
    eva5 = models.IntegerField(null=True)
    eva6 = models.IntegerField(null=True)
    eva7 = models.IntegerField(null=True)


class Review3(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=20, null=True)
    review = models.TextField(null=True)
    date_time = models.DateTimeField(null=True)
    eva1 = models.IntegerField(null=True)
    eva2 = models.IntegerField(null=True)
    eva3 = models.IntegerField(null=True)
    eva4 = models.IntegerField(null=True)
    eva5 = models.IntegerField(null=True)
    eva6 = models.IntegerField(null=True)
    eva7 = models.IntegerField(null=True)


class Review4(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=20, null=True)
    review = models.TextField(null=True)
    date_time = models.DateTimeField(null=True)
    eva1 = models.IntegerField(null=True)
    eva2 = models.IntegerField(null=True)
    eva3 = models.IntegerField(null=True)
    eva4 = models.IntegerField(null=True)
    eva5 = models.IntegerField(null=True)
    eva6 = models.IntegerField(null=True)
    eva7 = models.IntegerField(null=True)


class Evaluation(models.Model):
	hotel_name = models.CharField(max_length=20, null=True)
	eva1 = models.DecimalField(max_digits=3, decimal_places=2, null=True)
	eva2 = models.DecimalField(max_digits=3, decimal_places=2, null=True)
	eva3 = models.DecimalField(max_digits=3, decimal_places=2, null=True)
	eva4 = models.DecimalField(max_digits=3, decimal_places=2, null=True)
	eva5 = models.DecimalField(max_digits=3, decimal_places=2, null=True)
	eva6 = models.DecimalField(max_digits=3, decimal_places=2, null=True)
	eva7 = models.DecimalField(max_digits=3, decimal_places=2, null=True)
	img_eva1 = models.CharField(max_length=3, null=True)
	img_eva2 = models.CharField(max_length=3, null=True)
	img_eva3 = models.CharField(max_length=3, null=True)
	img_eva4 = models.CharField(max_length=3, null=True)
	img_eva5 = models.CharField(max_length=3, null=True)
	img_eva6 = models.CharField(max_length=3, null=True)
	img_eva7 = models.CharField(max_length=3, null=True)


class TopicSummarize(models.Model):
	topic_id = models.IntegerField(null=True)
	word1 = models.TextField(null=True)
	word2 = models.TextField(null=True)
	word3 = models.TextField(null=True)
	word4 = models.TextField(null=True)
	word5 = models.TextField(null=True)
	word6 = models.TextField(null=True)
	word7 = models.TextField(null=True)
	word8 = models.TextField(null=True)


class SummarizeReview1(models.Model):
	doc_id = models.IntegerField(null=True)
	topic_id = models.IntegerField(null=True)
	user_name = models.CharField(max_length=20, null=True)
	date_time = models.DateTimeField(null=True)
	sentence = models.TextField(null=True)
	method_name = models.CharField(max_length=20, null=True)


class SummarizeReview2(models.Model):
	doc_id = models.IntegerField(null=True)
	topic_id = models.IntegerField(null=True)
	user_name = models.CharField(max_length=20, null=True)
	date_time = models.DateTimeField(null=True)
	sentence = models.TextField(null=True)
	method_name = models.CharField(max_length=20, null=True)


class SummarizeReview_exp2(models.Model):
	doc_id = models.IntegerField(null=True)
	topic_id = models.IntegerField(null=True)
	hotel_name = models.CharField(max_length=20, null=True)
	user_name = models.CharField(max_length=20, null=True)
	date_time = models.DateTimeField(null=True)
	sentence = models.TextField(null=True)
	method_name = models.CharField(max_length=20, null=True)
	review = models.TextField(null=True)
	eva7 = models.IntegerField(null=True)


class Sentence1(models.Model):
	topic_id = models.IntegerField(null=True)
	user_name = models.CharField(max_length=20, null=True)
	date_time = models.DateTimeField(null=True)
	sentence = models.TextField(null=True)


class Sentence2(models.Model):
	topic_id = models.IntegerField(null=True)
	user_name = models.CharField(max_length=20, null=True)
	date_time = models.DateTimeField(null=True)
	sentence = models.TextField(null=True)


class Questionnaire1(models.Model):
	user_name = models.CharField(max_length=20, null=True)
	start_time = models.DateTimeField(null=True)
	end_time = models.DateTimeField(default=datetime.now, null=True)
	passwd = models.CharField(max_length=20, null=True)
	q2_1 = models.TextField(null=True)
	q2_2 = models.TextField(null=True)
	q2_3 = models.TextField(null=True)
	q2_4 = models.TextField(null=True)

	q3_1 = models.TextField(null=True)
	q3_2 = models.TextField(null=True)
	q3_3 = models.TextField(null=True)
	q3_4 = models.TextField(null=True)

	q4_1 = models.TextField(null=True)
	q4_2 = models.TextField(null=True)
	q4_3 = models.TextField(null=True)
	q4_4 = models.TextField(null=True)

	q5 = models.TextField(null=True)

	q6 = models.TextField(null=True)

	q7_1 = models.IntegerField(null=True)
	q7_2 = models.IntegerField(null=True)
	q7_3 = models.IntegerField(null=True)
	q7_4 = models.IntegerField(null=True)

	q8_1 = models.IntegerField(null=True)
	q8_2 = models.IntegerField(null=True)
	q8_3 = models.IntegerField(null=True)
	q8_4 = models.IntegerField(null=True)

	q9_1 = models.IntegerField(null=True)
	q9_2 = models.IntegerField(null=True)
	q9_3 = models.IntegerField(null=True)
	q9_4 = models.IntegerField(null=True)

	q10_1 = models.IntegerField(null=True)
	q10_2 = models.IntegerField(null=True)
	q10_3 = models.IntegerField(null=True)
	q10_4 = models.IntegerField(null=True)

	q11_1 = models.IntegerField(null=True)
	q11_2 = models.IntegerField(null=True)
	q11_3 = models.IntegerField(null=True)
	q11_4 = models.IntegerField(null=True)

	q12_1 = models.IntegerField(null=True)
	q12_2 = models.IntegerField(null=True)
	q12_3 = models.IntegerField(null=True)
	q12_4 = models.IntegerField(null=True)

	q13_1 = models.IntegerField(null=True)
	q13_2 = models.IntegerField(null=True)
	q13_3 = models.IntegerField(null=True)
	q13_4 = models.IntegerField(null=True)

	q14_1 = models.IntegerField(null=True)
	q14_2 = models.IntegerField(null=True)
	q14_3 = models.IntegerField(null=True)
	q14_4 = models.IntegerField(null=True)

	q15_1 = models.IntegerField(null=True)
	q15_2 = models.IntegerField(null=True)
	q15_3 = models.IntegerField(null=True)
	q15_4 = models.IntegerField(null=True)

	q16_1 = models.IntegerField(null=True)
	q16_2 = models.IntegerField(null=True)
	q16_3 = models.IntegerField(null=True)
	q16_4 = models.IntegerField(null=True)

	q17_1 = models.IntegerField(null=True)
	q17_2 = models.IntegerField(null=True)
	q17_3 = models.IntegerField(null=True)
	q17_4 = models.IntegerField(null=True)

	q18_1 = models.IntegerField(null=True)
	q18_2 = models.IntegerField(null=True)
	q18_3 = models.IntegerField(null=True)
	q18_4 = models.IntegerField(null=True)

	q19_1 = models.IntegerField(null=True)
	q19_2 = models.IntegerField(null=True)
	q19_3 = models.IntegerField(null=True)
	q19_4 = models.IntegerField(null=True)

	q20_1 = models.IntegerField(null=True)
	q20_2 = models.IntegerField(null=True)
	q20_3 = models.IntegerField(null=True)
	q20_4 = models.IntegerField(null=True)

	q21_1 = models.IntegerField(null=True)
	q21_2 = models.IntegerField(null=True)
	q21_3 = models.IntegerField(null=True)
	q21_4 = models.IntegerField(null=True)

	q22_1 = models.IntegerField(null=True)
	q22_2 = models.IntegerField(null=True)
	q22_3 = models.IntegerField(null=True)
	q22_4 = models.IntegerField(null=True)

	q23_1 = models.IntegerField(null=True)
	q23_2 = models.IntegerField(null=True)
	q23_3 = models.IntegerField(null=True)
	q23_4 = models.IntegerField(null=True)

	q24_1 = models.IntegerField(null=True)
	q24_2 = models.IntegerField(null=True)
	q24_3 = models.IntegerField(null=True)
	q24_4 = models.IntegerField(null=True)

	q25_1 = models.IntegerField(null=True)
	q25_2 = models.IntegerField(null=True)
	q25_3 = models.IntegerField(null=True)
	q25_4 = models.IntegerField(null=True)

	q26_1 = models.IntegerField(null=True)
	q26_2 = models.IntegerField(null=True)
	q26_3 = models.IntegerField(null=True)
	q26_4 = models.IntegerField(null=True)

	q27_1 = models.IntegerField(null=True)
	q27_2 = models.IntegerField(null=True)
	q27_3 = models.IntegerField(null=True)
	q27_4 = models.IntegerField(null=True)

	q28_1 = models.IntegerField(null=True)
	q28_2 = models.IntegerField(null=True)
	q28_3 = models.IntegerField(null=True)
	q28_4 = models.IntegerField(null=True)

	q29_1 = models.IntegerField(null=True)
	q29_2 = models.IntegerField(null=True)
	q29_3 = models.IntegerField(null=True)
	q29_4 = models.IntegerField(null=True)

	q30_1 = models.IntegerField(null=True)
	q30_2 = models.IntegerField(null=True)
	q30_3 = models.IntegerField(null=True)
	q30_4 = models.IntegerField(null=True)

	q31_1 = models.IntegerField(null=True)
	q31_2 = models.IntegerField(null=True)
	q31_3 = models.IntegerField(null=True)
	q31_4 = models.IntegerField(null=True)

	q32_1 = models.IntegerField(null=True)
	q32_2 = models.IntegerField(null=True)
	q32_3 = models.IntegerField(null=True)
	q32_4 = models.IntegerField(null=True)

	q33_1 = models.IntegerField(null=True)
	q33_2 = models.IntegerField(null=True)
	q33_3 = models.IntegerField(null=True)
	q33_4 = models.IntegerField(null=True)

	q34_1 = models.IntegerField(null=True)
	q34_2 = models.IntegerField(null=True)
	q34_3 = models.IntegerField(null=True)
	q34_4 = models.IntegerField(null=True)

	q35_1 = models.IntegerField(null=True)
	q35_2 = models.IntegerField(null=True)
	q35_3 = models.IntegerField(null=True)
	q35_4 = models.IntegerField(null=True)

	q36_1 = models.IntegerField(null=True)
	q36_2 = models.IntegerField(null=True)
	q36_3 = models.IntegerField(null=True)
	q36_4 = models.IntegerField(null=True)

	q37_1 = models.IntegerField(null=True)
	q37_2 = models.IntegerField(null=True)
	q37_3 = models.IntegerField(null=True)
	q37_4 = models.IntegerField(null=True)


class Questionnaire2(models.Model):
	user_name = models.CharField(max_length=20, null=True)
	passwd = models.CharField(max_length=20, null=True)

	q1_1 = models.IntegerField(null=True)
	q1_2 = models.IntegerField(null=True)

	q2_1 = models.IntegerField(null=True)
	q2_2 = models.IntegerField(null=True)

	q3_1 = models.IntegerField(null=True)
	q3_2 = models.IntegerField(null=True)

	q4_1 = models.IntegerField(null=True)
	q4_2 = models.IntegerField(null=True)

	q5_1 = models.IntegerField(null=True)
	q5_2 = models.IntegerField(null=True)

	q6_1 = models.IntegerField(null=True)
	q6_2 = models.IntegerField(null=True)

	q7_1 = models.IntegerField(null=True)
	q7_2 = models.IntegerField(null=True)

	q8_1 = models.IntegerField(null=True)
	q8_2 = models.IntegerField(null=True)

	q9_1 = models.IntegerField(null=True)
	q9_2 = models.IntegerField(null=True)

	q10_1 = models.IntegerField(null=True)
	q10_2 = models.IntegerField(null=True)

	q11_1 = models.IntegerField(null=True)
	q11_2 = models.IntegerField(null=True)

	q12_1 = models.IntegerField(null=True)
	q12_2 = models.IntegerField(null=True)

	q13_1 = models.IntegerField(null=True)
	q13_2 = models.IntegerField(null=True)

	q14_1 = models.IntegerField(null=True)
	q14_2 = models.IntegerField(null=True)

	q15_1 = models.IntegerField(null=True)
	q15_2 = models.IntegerField(null=True)

	q16_1 = models.IntegerField(null=True)
	q16_2 = models.IntegerField(null=True)

	q17_1 = models.IntegerField(null=True)
	q17_2 = models.IntegerField(null=True)

	q18_1 = models.IntegerField(null=True)
	q18_2 = models.IntegerField(null=True)

	q19_1 = models.IntegerField(null=True)
	q19_2 = models.IntegerField(null=True)

	q20_1 = models.IntegerField(null=True)
	q20_2 = models.IntegerField(null=True)

	q21_1 = models.IntegerField(null=True)
	q21_2 = models.IntegerField(null=True)

	q22_1 = models.IntegerField(null=True)
	q22_2 = models.IntegerField(null=True)

	q23_1 = models.IntegerField(null=True)
	q23_2 = models.IntegerField(null=True)

	q24_1 = models.IntegerField(null=True)
	q24_2 = models.IntegerField(null=True)

	q25_1 = models.IntegerField(null=True)
	q25_2 = models.IntegerField(null=True)

	q26_1 = models.IntegerField(null=True)
	q26_2 = models.IntegerField(null=True)

	q27_1 = models.IntegerField(null=True)
	q27_2 = models.IntegerField(null=True)

	q28_1 = models.IntegerField(null=True)
	q28_2 = models.IntegerField(null=True)

	q29_1 = models.IntegerField(null=True)
	q29_2 = models.IntegerField(null=True)

	q30_1 = models.IntegerField(null=True)
	q30_2 = models.IntegerField(null=True)

	q31_1 = models.IntegerField(null=True)
	q31_2 = models.IntegerField(null=True)

	q32_1 = models.IntegerField(null=True)
	q32_2 = models.IntegerField(null=True)

	q33_1 = models.IntegerField(null=True)
	q33_2 = models.IntegerField(null=True)

	q34_1 = models.IntegerField(null=True)
	q34_2 = models.IntegerField(null=True)

	q35_1 = models.IntegerField(null=True)
	q35_2 = models.IntegerField(null=True)

	q36_1 = models.IntegerField(null=True)
	q36_2 = models.IntegerField(null=True)

	q37_1 = models.IntegerField(null=True)
	q37_2 = models.IntegerField(null=True)

	q38_1 = models.IntegerField(null=True)
	q38_2 = models.IntegerField(null=True)

	q39_1 = models.IntegerField(null=True)
	q39_2 = models.IntegerField(null=True)

	q40_1 = models.IntegerField(null=True)
	q40_2 = models.IntegerField(null=True)

	q41_1 = models.IntegerField(null=True)
	q41_2 = models.IntegerField(null=True)

	q42_1 = models.IntegerField(null=True)
	q42_2 = models.IntegerField(null=True)

	q43_1 = models.IntegerField(null=True)
	q43_2 = models.IntegerField(null=True)

	q44_1 = models.IntegerField(null=True)
	q44_2 = models.IntegerField(null=True)

	q45_1 = models.IntegerField(null=True)
	q45_2 = models.IntegerField(null=True)

	q46_1 = models.IntegerField(null=True)
	q46_2 = models.IntegerField(null=True)

	q47_1 = models.IntegerField(null=True)
	q47_2 = models.IntegerField(null=True)

	q48_1 = models.IntegerField(null=True)
	q48_2 = models.IntegerField(null=True)

	q49_1 = models.IntegerField(null=True)
	q49_2 = models.IntegerField(null=True)

	q50_1 = models.IntegerField(null=True)
	q50_2 = models.IntegerField(null=True)

	q51_1 = models.IntegerField(null=True)
	q51_2 = models.IntegerField(null=True)

	q52_1 = models.IntegerField(null=True)
	q52_2 = models.IntegerField(null=True)

	q53_1 = models.IntegerField(null=True)
	q53_2 = models.IntegerField(null=True)

	q54_1 = models.IntegerField(null=True)
	q54_2 = models.IntegerField(null=True)

	q55_1 = models.IntegerField(null=True)
	q55_2 = models.IntegerField(null=True)

	q56_1 = models.IntegerField(null=True)
	q56_2 = models.IntegerField(null=True)

	q57_1 = models.IntegerField(null=True)
	q57_2 = models.IntegerField(null=True)

	q58_1 = models.IntegerField(null=True)
	q58_2 = models.IntegerField(null=True)

	q59_1 = models.IntegerField(null=True)
	q59_2 = models.IntegerField(null=True)

	q60_1 = models.IntegerField(null=True)
	q60_2 = models.IntegerField(null=True)

	q61_1 = models.IntegerField(null=True)
	q61_2 = models.IntegerField(null=True)

	q62_1 = models.IntegerField(null=True)
	q62_2 = models.IntegerField(null=True)


class Questionnaire_exp2(models.Model):
	meta1 = models.IntegerField('meta1', null=True)
	meta2 = models.DateTimeField('start_time', null=True)
	meta3 = models.DateTimeField('end_time', null=True)
	passwd = models.CharField(max_length=20, null=True)
	q1 = models.CharField('question1', max_length=20, null=True)
	q2 = models.IntegerField('question2', null=True)
	q3 = models.IntegerField('question3', null=True)
	q4 = models.IntegerField('question4', null=True)
	q5 = models.IntegerField('question5', null=True)
	q6 = models.IntegerField('question6', null=True)
	q7 = models.IntegerField('question7', null=True)
	q8 = models.IntegerField('question8', null=True)
	q9 = models.IntegerField('question9', null=True)
	q10 = models.IntegerField('question10', null=True)
	q11 = models.IntegerField('question11', null=True)
	q12 = models.IntegerField('question12', null=True)
	q13 = models.IntegerField('question13', null=True)
	q14 = models.IntegerField('question14', null=True)
	q15 = models.IntegerField('question15', null=True)
	q16 = models.IntegerField('question16', null=True)
	q17 = models.IntegerField('question17', null=True)
	q18 = models.IntegerField('question18', null=True)
	q19 = models.IntegerField('question19', null=True)
	q20 = models.IntegerField('question20', null=True)
	q21 = models.IntegerField('question21', null=True)
	q22 = models.IntegerField('question22', null=True)
	q23 = models.IntegerField('question23', null=True)
	q24 = models.IntegerField('question24', null=True)
	q25 = models.IntegerField('question25', null=True)
	q26 = models.IntegerField('question26', null=True)
	q27 = models.IntegerField('question27', null=True)
	q28 = models.IntegerField('question28', null=True)
	q29 = models.IntegerField('question29', null=True)
	q30 = models.IntegerField('question30', null=True)
	q31 = models.IntegerField('question31', null=True)
	q32 = models.IntegerField('question32', null=True)
	q33 = models.IntegerField('question33', null=True)
	q34 = models.IntegerField('question34', null=True)
	q35 = models.IntegerField('question35', null=True)

	q36_1 = models.IntegerField('question36_1', null=True)
	q36_2 = models.TextField('question36_2', null=True)
	q37_1 = models.IntegerField('question37_1', null=True)
	q37_2 = models.TextField('question37_2', null=True)
	q38_1 = models.IntegerField('question38_1', null=True)
	q38_2 = models.TextField('question38_2', null=True)
	q39_1 = models.IntegerField('question39_1', null=True)
	q39_2 = models.TextField('question39_2', null=True)

	q40 = models.IntegerField('question40', null=True)
	q41 = models.IntegerField('question41', null=True)
	q42_1 = models.IntegerField('question42_1', null=True)
	q42_2 = models.IntegerField('question42_2', null=True)
	q42_3 = models.IntegerField('question42_3', null=True)


class Questionnaire_exp3(models.Model):
	user_name = models.CharField(max_length=20, null=True)
	passwd = models.CharField(max_length=20, null=True)
	meta2 = models.DateTimeField('start_time', null=True)
	meta3 = models.DateTimeField('end_time', null=True)

	q1_1 = models.IntegerField(null=True)
	q1_2 = models.IntegerField(null=True)

	q2_1 = models.IntegerField(null=True)
	q2_2 = models.IntegerField(null=True)

	q3_1 = models.IntegerField(null=True)
	q3_2 = models.IntegerField(null=True)

	q4_1 = models.IntegerField(null=True)
	q4_2 = models.IntegerField(null=True)

	q5_1 = models.IntegerField(null=True)
	q5_2 = models.IntegerField(null=True)

	q6_1 = models.IntegerField(null=True)
	q6_2 = models.IntegerField(null=True)

	q7_1 = models.IntegerField(null=True)
	q7_2 = models.IntegerField(null=True)

	q8_1 = models.IntegerField(null=True)
	q8_2 = models.IntegerField(null=True)

	q9_1 = models.IntegerField(null=True)
	q9_2 = models.IntegerField(null=True)

	q10_1 = models.IntegerField(null=True)
	q10_2 = models.IntegerField(null=True)

	q11_1 = models.IntegerField(null=True)
	q11_2 = models.IntegerField(null=True)

	q12_1 = models.IntegerField(null=True)
	q12_2 = models.IntegerField(null=True)

	q13_1 = models.IntegerField(null=True)
	q13_2 = models.IntegerField(null=True)

	q14_1 = models.IntegerField(null=True)
	q14_2 = models.IntegerField(null=True)

	q15_1 = models.IntegerField(null=True)
	q15_2 = models.IntegerField(null=True)

	q16_1 = models.IntegerField(null=True)
	q16_2 = models.IntegerField(null=True)

	q17_1 = models.IntegerField(null=True)
	q17_2 = models.IntegerField(null=True)

	q18_1 = models.IntegerField(null=True)
	q18_2 = models.IntegerField(null=True)

	q19_1 = models.IntegerField(null=True)
	q19_2 = models.IntegerField(null=True)

	q20_1 = models.IntegerField(null=True)
	q20_2 = models.IntegerField(null=True)

	q21_1 = models.IntegerField(null=True)
	q21_2 = models.IntegerField(null=True)

	q22_1 = models.IntegerField(null=True)
	q22_2 = models.IntegerField(null=True)

	q23_1 = models.IntegerField(null=True)
	q23_2 = models.IntegerField(null=True)

	q24_1 = models.IntegerField(null=True)
	q24_2 = models.IntegerField(null=True)

	q25_1 = models.IntegerField(null=True)
	q25_2 = models.IntegerField(null=True)

	q26_1 = models.IntegerField(null=True)
	q26_2 = models.IntegerField(null=True)

	q27_1 = models.IntegerField(null=True)
	q27_2 = models.IntegerField(null=True)

	q28_1 = models.IntegerField(null=True)
	q28_2 = models.IntegerField(null=True)

	q29_1 = models.IntegerField(null=True)
	q29_2 = models.IntegerField(null=True)

	q30_1 = models.IntegerField(null=True)
	q30_2 = models.IntegerField(null=True)

	q31_1 = models.IntegerField(null=True)
	q31_2 = models.IntegerField(null=True)

	q32_1 = models.TextField('question32_1', null=True)
	q32_2 = models.TextField('question32_2', null=True)

	q33_1 = models.TextField('question33_1', null=True)
	q33_2 = models.TextField('question33_2', null=True)
