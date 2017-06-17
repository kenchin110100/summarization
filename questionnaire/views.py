# coding: utf-8
from django.shortcuts import render
from questionnaire.models import Review1, Review2, Evaluation, SummarizeReview1, SummarizeReview2, TopicSummarize, Review3, Review4, SummarizeReview_exp2
import datetime
from django.shortcuts import redirect
from . import forms, models
import random

# Create your views here.


def home(request):
    d = {'title': 'アンケート',
         'content1': 'アンケート1',
         'url1': 'http://www.orenotame.com/questionnaire/questionnaire1',
         'date1': '2016/09/18'}
    return render(request, 'index_q.html', d)


def index1(request):
    return render(request, 'index1.html')


def index2(request):
    return render(request, 'index2.html')


def index_exp2(request):
    return render(request, 'index_exp2.html')


def review1(request):
    list_d1 = Review1.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation1 = Evaluation.objects.get(hotel_name='ホテルA')
    num1_5 = list_d1.filter(eva7=5).count()
    num1_4 = list_d1.filter(eva7=4).count()
    num1_3 = list_d1.filter(eva7=3).count()
    num1_2 = list_d1.filter(eva7=2).count()
    num1_1 = list_d1.filter(eva7=1).count()
    list_d2 = Review2.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation2 = Evaluation.objects.get(hotel_name='ホテルB')
    num2_5 = list_d2.filter(eva7=5).count()
    num2_4 = list_d2.filter(eva7=4).count()
    num2_3 = list_d2.filter(eva7=3).count()
    num2_2 = list_d2.filter(eva7=2).count()
    num2_1 = list_d2.filter(eva7=1).count()
    list_sum1 = SummarizeReview1.objects.all()
    sum1_SM = list_sum1.filter(method_name='SM')
    sum1_PGSM = list_sum1.filter(method_name='PGSM')
    sum1_PGSM_topic = list_sum1.filter(method_name='PGSM_topic')
    list_sum2 = SummarizeReview2.objects.all()
    sum2_SM = list_sum2.filter(method_name='SM')
    sum2_PGSM = list_sum2.filter(method_name='PGSM')
    sum2_PGSM_topic = list_sum2.filter(method_name='PGSM_topic')
    topic_name = TopicSummarize.objects.all()
    d = {'review1': list_d1,
         'evaluation1': evaluation1,
         'num1_5': num1_5,
         'num1_4': num1_4,
         'num1_3': num1_3,
         'num1_2': num1_2,
         'num1_1': num1_1,
         'review2': list_d2,
         'evaluation2': evaluation2,
         'num2_5': num2_5,
         'num2_4': num2_4,
         'num2_3': num2_3,
         'num2_2': num2_2,
         'num2_1': num2_1,
         'sum1_SM': sum1_SM,
         'sum1_PGSM': sum1_PGSM,
         'sum1_PGSM_topic1': sum1_PGSM_topic.filter(topic_id=1),
         'sum1_PGSM_topic2': sum1_PGSM_topic.filter(topic_id=2),
         'sum1_PGSM_topic3': sum1_PGSM_topic.filter(topic_id=3),
         'sum1_PGSM_topic4': sum1_PGSM_topic.filter(topic_id=4),
         'sum1_PGSM_topic5': sum1_PGSM_topic.filter(topic_id=5),
         'sum1_PGSM_topic6': sum1_PGSM_topic.filter(topic_id=6),
         'sum1_PGSM_topic7': sum1_PGSM_topic.filter(topic_id=7),
         'sum2_SM': sum2_SM,
         'sum2_PGSM': sum2_PGSM,
         'sum2_PGSM_topic1': sum2_PGSM_topic.filter(topic_id=1),
         'sum2_PGSM_topic2': sum2_PGSM_topic.filter(topic_id=2),
         'sum2_PGSM_topic3': sum2_PGSM_topic.filter(topic_id=3),
         'sum2_PGSM_topic4': sum2_PGSM_topic.filter(topic_id=4),
         'sum2_PGSM_topic5': sum2_PGSM_topic.filter(topic_id=5),
         'sum2_PGSM_topic6': sum2_PGSM_topic.filter(topic_id=6),
         'sum2_PGSM_topic7': sum2_PGSM_topic.filter(topic_id=7),
         'topic_name1': topic_name.get(topic_id=1),
         'topic_name2': topic_name.get(topic_id=2),
         'topic_name3': topic_name.get(topic_id=3),
         'topic_name4': topic_name.get(topic_id=4),
         'topic_name5': topic_name.get(topic_id=5),
         'topic_name6': topic_name.get(topic_id=6),
         'topic_name7': topic_name.get(topic_id=7)}
    return render(request, 'review1.html', d)

def review2(request):
    list_d1 = Review1.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation1 = Evaluation.objects.get(hotel_name='ホテルA')
    list_d2 = Review2.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation2 = Evaluation.objects.get(hotel_name='ホテルB')
    list_d3 = Review3.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation3 = Evaluation.objects.get(hotel_name='ホテルC')
    list_d4 = Review4.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation4 = Evaluation.objects.get(hotel_name='ホテルD')
    list_sum = SummarizeReview_exp2.objects.all()
    list_sum1 = list_sum.filter(hotel_name='ホテルA')
    list_sum2 = list_sum.filter(hotel_name='ホテルB')
    list_sum3 = list_sum.filter(hotel_name='ホテルC')
    list_sum4 = list_sum.filter(hotel_name='ホテルD')
    random_index = random.randint(1,2)
    d = {'review1': list_d1,
         'evaluation1': evaluation1,
         'num1_5': list_d1.filter(eva7=5).count(),
         'num1_4': list_d1.filter(eva7=4).count(),
         'num1_3': list_d1.filter(eva7=3).count(),
         'num1_2': list_d1.filter(eva7=2).count(),
         'num1_1': list_d1.filter(eva7=1).count(),
         'review2': list_d2,
         'evaluation2': evaluation2,
         'num2_5': list_d2.filter(eva7=5).count(),
         'num2_4': list_d2.filter(eva7=4).count(),
         'num2_3': list_d2.filter(eva7=3).count(),
         'num2_2': list_d2.filter(eva7=2).count(),
         'num2_1': list_d2.filter(eva7=1).count(),
         'review3': list_d3,
         'evaluation3': evaluation3,
         'num3_5': list_d3.filter(eva7=5).count(),
         'num3_4': list_d3.filter(eva7=4).count(),
         'num3_3': list_d3.filter(eva7=3).count(),
         'num3_2': list_d3.filter(eva7=2).count(),
         'num3_1': list_d3.filter(eva7=1).count(),
         'review4': list_d4,
         'evaluation4': evaluation4,
         'num4_5': list_d4.filter(eva7=5).count(),
         'num4_4': list_d4.filter(eva7=4).count(),
         'num4_3': list_d4.filter(eva7=3).count(),
         'num4_2': list_d4.filter(eva7=2).count(),
         'num4_1': list_d4.filter(eva7=1).count(),
         'sum1_topic1': list_sum1.filter(topic_id=1).order_by('doc_id')[:3],
         'sum1_topic2': list_sum1.filter(topic_id=2).order_by('doc_id')[:3],
         'sum1_topic3': list_sum1.filter(topic_id=3).order_by('doc_id')[:3],
         'sum1_topic4': list_sum1.filter(topic_id=4).order_by('doc_id')[:3],
         'sum1_topic5': list_sum1.filter(topic_id=5).order_by('doc_id')[:3],
         'sum1_topic6': list_sum1.filter(topic_id=6).order_by('doc_id')[:3],
         'sum1_topic7': list_sum1.filter(topic_id=7).order_by('doc_id')[:3],
         'sum2_topic1': list_sum2.filter(topic_id=1).order_by('doc_id')[:3],
         'sum2_topic2': list_sum2.filter(topic_id=2).order_by('doc_id')[:3],
         'sum2_topic3': list_sum2.filter(topic_id=3).order_by('doc_id')[:3],
         'sum2_topic4': list_sum2.filter(topic_id=4).order_by('doc_id')[:3],
         'sum2_topic5': list_sum2.filter(topic_id=5).order_by('doc_id')[:3],
         'sum2_topic6': list_sum2.filter(topic_id=6).order_by('doc_id')[:3],
         'sum2_topic7': list_sum2.filter(topic_id=7).order_by('doc_id')[:3],
         'sum3_topic1': list_sum3.filter(topic_id=1).order_by('doc_id')[:3],
         'sum3_topic2': list_sum3.filter(topic_id=2).order_by('doc_id')[:3],
         'sum3_topic3': list_sum3.filter(topic_id=3).order_by('doc_id')[:3],
         'sum3_topic4': list_sum3.filter(topic_id=4).order_by('doc_id')[:3],
         'sum3_topic5': list_sum3.filter(topic_id=5).order_by('doc_id')[:3],
         'sum3_topic6': list_sum3.filter(topic_id=6).order_by('doc_id')[:3],
         'sum3_topic7': list_sum3.filter(topic_id=7).order_by('doc_id')[:3],
         'sum4_topic1': list_sum4.filter(topic_id=1).order_by('doc_id')[:3],
         'sum4_topic2': list_sum4.filter(topic_id=2).order_by('doc_id')[:3],
         'sum4_topic3': list_sum4.filter(topic_id=3).order_by('doc_id')[:3],
         'sum4_topic4': list_sum4.filter(topic_id=4).order_by('doc_id')[:3],
         'sum4_topic5': list_sum4.filter(topic_id=5).order_by('doc_id')[:3],
         'sum4_topic6': list_sum4.filter(topic_id=6).order_by('doc_id')[:3],
         'sum4_topic7': list_sum4.filter(topic_id=7).order_by('doc_id')[:3],
         'random_index': random_index}
    return render(request, 'review_exp2_%s.html' % random_index, d)


def review(request):
    list_d1 = Review1.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation1 = Evaluation.objects.get(hotel_name='ホテルA')
    num1_5 = list_d1.filter(eva7=5).count()
    num1_4 = list_d1.filter(eva7=4).count()
    num1_3 = list_d1.filter(eva7=3).count()
    num1_2 = list_d1.filter(eva7=2).count()
    num1_1 = list_d1.filter(eva7=1).count()
    list_d2 = Review2.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation2 = Evaluation.objects.get(hotel_name='ホテルB')
    num2_5 = list_d2.filter(eva7=5).count()
    num2_4 = list_d2.filter(eva7=4).count()
    num2_3 = list_d2.filter(eva7=3).count()
    num2_2 = list_d2.filter(eva7=2).count()
    num2_1 = list_d2.filter(eva7=1).count()
    list_sum1 = SummarizeReview1.objects.all()
    sum1_SM = list_sum1.filter(method_name='SM')
    sum1_PGSM = list_sum1.filter(method_name='PGSM')
    sum1_PGSM_topic = list_sum1.filter(method_name='PGSM_topic')
    list_sum2 = SummarizeReview2.objects.all()
    sum2_SM = list_sum2.filter(method_name='SM')
    sum2_PGSM = list_sum2.filter(method_name='PGSM')
    sum2_PGSM_topic = list_sum2.filter(method_name='PGSM_topic')
    topic_name = TopicSummarize.objects.all()
    random_index = random.randint(1,2)
    d = {'review1': list_d1,
         'evaluation1': evaluation1,
         'num1_5': num1_5,
         'num1_4': num1_4,
         'num1_3': num1_3,
         'num1_2': num1_2,
         'num1_1': num1_1,
         'review2': list_d2,
         'evaluation2': evaluation2,
         'num2_5': num2_5,
         'num2_4': num2_4,
         'num2_3': num2_3,
         'num2_2': num2_2,
         'num2_1': num2_1,
         'sum1_SM': sum1_SM,
         'sum1_PGSM': sum1_PGSM,
         'sum1_PGSM_topic1': sum1_PGSM_topic.filter(topic_id=1),
         'sum1_PGSM_topic2': sum1_PGSM_topic.filter(topic_id=2),
         'sum1_PGSM_topic3': sum1_PGSM_topic.filter(topic_id=3),
         'sum1_PGSM_topic4': sum1_PGSM_topic.filter(topic_id=4),
         'sum1_PGSM_topic5': sum1_PGSM_topic.filter(topic_id=5),
         'sum1_PGSM_topic6': sum1_PGSM_topic.filter(topic_id=6),
         'sum1_PGSM_topic7': sum1_PGSM_topic.filter(topic_id=7),
         'sum2_SM': sum2_SM,
         'sum2_PGSM': sum2_PGSM,
         'sum2_PGSM_topic1': sum2_PGSM_topic.filter(topic_id=1),
         'sum2_PGSM_topic2': sum2_PGSM_topic.filter(topic_id=2),
         'sum2_PGSM_topic3': sum2_PGSM_topic.filter(topic_id=3),
         'sum2_PGSM_topic4': sum2_PGSM_topic.filter(topic_id=4),
         'sum2_PGSM_topic5': sum2_PGSM_topic.filter(topic_id=5),
         'sum2_PGSM_topic6': sum2_PGSM_topic.filter(topic_id=6),
         'sum2_PGSM_topic7': sum2_PGSM_topic.filter(topic_id=7),
         'topic_name1': topic_name.get(topic_id=1),
         'topic_name2': topic_name.get(topic_id=2),
         'topic_name3': topic_name.get(topic_id=3),
         'topic_name4': topic_name.get(topic_id=4),
         'topic_name5': topic_name.get(topic_id=5),
         'topic_name6': topic_name.get(topic_id=6),
         'topic_name7': topic_name.get(topic_id=7),
         'random_index': random_index}
    return render(request, 'review.html', d)



def consent(request):
    if request.method == 'POST':
        return redirect('questionnaire:review')
    else:
        return render(request, 'consent.html')


def questionnaire1(request):
    form = forms.Questionnaire2(request.POST or None)
    d = {'form': form,
        'message': ''}
    if form.is_valid():
        passwd = make_passwd()
        d = {'passwd': passwd}
        form.cleaned_data['passwd'] = passwd
        models.Questionnaire2.objects.create(**form.cleaned_data)
        return render(request, 'passwd.html', d)
    elif request.method == 'POST':
        d['message'] = '入力されていないフォームが存在します'
        return render(request, 'questionnaire_1.html', d)
    else:
        return render(request, 'questionnaire_1.html', d)


def questionnaire2(request):
    form = forms.Questionnaire2(request.POST or None)
    d = {'form': form,
        'message': ''}
    if form.is_valid():
        passwd = make_passwd()
        d = {'passwd': passwd}
        form.cleaned_data['passwd'] = passwd
        models.Questionnaire2.objects.create(**form.cleaned_data)
        return render(request, 'passwd.html', d)
    elif request.method == 'POST':
        d['message'] = '入力されていないフォームが存在します'
        return render(request, 'questionnaire_2.html', d)
    else:
        return render(request, 'questionnaire_2.html', d)


def questionnaire_exp2(request):
    form = forms.Questionnaire_exp2(request.POST or None)
    d = {'form': form,
         'message': ''}
    if form.is_valid():
        passwd = make_passwd()
        d = {'passwd': passwd}
        form.cleaned_data['passwd'] = passwd
        models.Questionnaire2.objects.create(**form.cleaned_data)
        return render(request, 'passwd.html', d)
    elif request.method == 'POST':
        d['message'] = '入力されていないフォームが存在します'
        return render(request, 'questionnaire_exp2.html', d)
    else:
        return render(request, 'questionnaire_exp2.html', d)


def make_passwd():
    list_tmp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'w', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(list_tmp)
    passwd = ''.join(list_tmp[0:8])
    return passwd
