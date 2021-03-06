# coding: utf-8
from django.shortcuts import render
from questionnaire.models import Evaluation, Review3, Review4, SummarizeReview_exp2
import datetime
from django.shortcuts import redirect
from . import models, forms_exp3
import random

# Create your views here.


def home(request):
    d = {'title': 'アンケート',
         'content1': 'アンケート1',
         'url1': 'http://www.orenotame.com/questionnaire/questionnaire1',
         'date1': '2016/09/18'}
    return render(request, 'index_q.html', d)


def index_exp3(request):
    return render(request, 'index_exp3.html')


def review_exp3(request):
    list_d3 = Review3.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation3 = Evaluation.objects.get(hotel_name='ホテルC')
    list_d4 = Review4.objects.filter(date_time__range=(datetime.date(2010, 9, 1), datetime.date(2010, 10, 31)))
    evaluation4 = Evaluation.objects.get(hotel_name='ホテルD')
    list_sum = SummarizeReview_exp2.objects.all()
    list_sum3 = list_sum.filter(hotel_name='ホテルC')
    list_sum4 = list_sum.filter(hotel_name='ホテルD')
    d = {'review3': list_d3,
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
         'sum3_topic1_1': list_sum3.filter(topic_id=1).order_by('doc_id')[:3],
         'sum3_topic2_1': list_sum3.filter(topic_id=2).order_by('doc_id')[:3],
         'sum3_topic3_1': list_sum3.filter(topic_id=3).order_by('doc_id')[:3],
         'sum3_topic4_1': list_sum3.filter(topic_id=4).order_by('doc_id')[:3],
         'sum3_topic5_1': list_sum3.filter(topic_id=5).order_by('doc_id')[:3],
         'sum3_topic6_1': list_sum3.filter(topic_id=6).order_by('doc_id')[:3],
         'sum3_topic7_1': list_sum3.filter(topic_id=7).order_by('doc_id')[:3],
         'sum3_topic1_2': list_sum3.filter(topic_id=1).order_by('doc_id')[3:],
         'sum3_topic2_2': list_sum3.filter(topic_id=2).order_by('doc_id')[3:],
         'sum3_topic3_2': list_sum3.filter(topic_id=3).order_by('doc_id')[3:],
         'sum3_topic4_2': list_sum3.filter(topic_id=4).order_by('doc_id')[3:],
         'sum3_topic5_2': list_sum3.filter(topic_id=5).order_by('doc_id')[3:],
         'sum3_topic6_2': list_sum3.filter(topic_id=6).order_by('doc_id')[3:],
         'sum3_topic7_2': list_sum3.filter(topic_id=7).order_by('doc_id')[3:],
         'sum4_topic1_1': list_sum4.filter(topic_id=1).order_by('doc_id')[:3],
         'sum4_topic2_1': list_sum4.filter(topic_id=2).order_by('doc_id')[:3],
         'sum4_topic3_1': list_sum4.filter(topic_id=3).order_by('doc_id')[:3],
         'sum4_topic4_1': list_sum4.filter(topic_id=4).order_by('doc_id')[:3],
         'sum4_topic5_1': list_sum4.filter(topic_id=5).order_by('doc_id')[:3],
         'sum4_topic6_1': list_sum4.filter(topic_id=6).order_by('doc_id')[:3],
         'sum4_topic7_1': list_sum4.filter(topic_id=7).order_by('doc_id')[:3],
         'sum4_topic1_2': list_sum4.filter(topic_id=1).order_by('doc_id')[3:],
         'sum4_topic2_2': list_sum4.filter(topic_id=2).order_by('doc_id')[3:],
         'sum4_topic3_2': list_sum4.filter(topic_id=3).order_by('doc_id')[3:],
         'sum4_topic4_2': list_sum4.filter(topic_id=4).order_by('doc_id')[3:],
         'sum4_topic5_2': list_sum4.filter(topic_id=5).order_by('doc_id')[3:],
         'sum4_topic6_2': list_sum4.filter(topic_id=6).order_by('doc_id')[3:],
         'sum4_topic7_2': list_sum4.filter(topic_id=7).order_by('doc_id')[3:],
         }
    return render(request, 'review_exp3.html', d)


def consent_exp3(request):
    if request.method == 'POST':
        return redirect('questionnaire:index_exp3')
    else:
        return render(request, 'consent_exp3.html')


def questionnaire_exp3(request):
    form = forms_exp3.Questionnaire_exp3(request.POST or None,
            initial = {'meta2': datetime.datetime.today()})
    d = {'form': form,
         'message': '',}
    if form.is_valid():
        passwd = make_passwd()
        d = {'passwd': passwd}
        form.cleaned_data['passwd'] = passwd
        form.cleaned_data['meta3'] = datetime.datetime.today()
        models.Questionnaire_exp3.objects.create(**form.cleaned_data)
        return render(request, 'passwd.html', d)
    elif request.method == 'POST':
        d['message'] = '入力されていないフォームが存在します'
        return render(request, 'questionnaire_exp3.html', d)
    else:
        return render(request, 'questionnaire_exp3.html', d)


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
