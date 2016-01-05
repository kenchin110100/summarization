# coding: utf-8
from django.shortcuts import render
from . import forms
from . import summarization
from . import summarization2
from functions.filer import Filer


# Create your views here.


def home(request):
    d = {
        'summarize': 'http://www.orenotame.com/summarization/summarize'
    }
    return render(request, 'index.html', d)


def hello_get_query(request):
    d = {
        'your_name': request.GET.get('your_name')
    }
    return render(request, 'get_query.html', d)


def hello_forms(request):
    form = forms.InputForm(request.POST or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'forms1.html', d)


def summarize(request):
    form = forms.InputForm(request.POST or None)
    list_num_sentence_S = []
    if form.is_valid():
        # 入力された値の取得
        input_text = form.cleaned_data['input_text']
        local_K = int(form.cleaned_data['K'])
        local_gamma = float(form.cleaned_data['gamma'])
        local_lamda = float(form.cleaned_data['lamda'])
        local_limit_sentence_num = int(form.cleaned_data['limit_sentence_num'])
        # 文字コードの変換
        total_sentence = Filer.conv(input_text)
        # インスタンス化
        summa = summarization.Summarization(local_K, local_gamma, local_lamda)
        summa.cal_greedy(total_sentence, limit_sentence_num=local_limit_sentence_num)
        list_sentence_S = summa.list_sentence_S
        message = 'クラスタ数: ' + str(local_K) + '    ' + 'γ: ' + str(local_gamma) + '    '  +'λ: ' + str(local_lamda) + '    ' + 'num_sentence: ' + str(local_limit_sentence_num)
        list_S = [num + 1 for num in summa.list_S]
        list_num_sentence_S.append(zip(list_S, list_sentence_S))
        d = {
			'form': form,
            'list_sentence_V': summa.list_sentence_V,
            'list_num_sentence_S': list_num_sentence_S,
            'message': message,
        }
        return render(request, 'forms1.html', d)
    else:
        message = '要約したい文書を入力してください'
    	d = {
            'form': form,
			'list_sentence_V': [],
			'list_num_sentence_S': list_num_sentence_S,
            'message': message,
        }
        return render(request, 'forms1.html', d)

def summarize2(request):
    form = forms.InputForm2(request.POST or None)
    list_num_sentence_S = []
    if form.is_valid():
        # 入力された値の取得
        input_text1 = form.cleaned_data['input_text1']
        input_text2 = form.cleaned_data['input_text2']
        local_K = int(form.cleaned_data['K'])
        local_gamma = float(form.cleaned_data['gamma'])
        local_epsilon = float(form.cleaned_data['epsilon'])
        local_lamda = float(form.cleaned_data['lamda'])
        local_limit_sentence_num = int(form.cleaned_data['limit_sentence_num'])
        # 文字コードの変換
        total_sentence1 = Filer.conv(input_text1)
        total_sentence2 = Filer.conv(input_text2)
        # インスタンス化
        summa = summarization2.Summarization2(local_K, local_gamma, local_epsilon, local_lamda)
        summa.cal_greedy(total_sentence1, total_sentence2, limit_sentence_num=local_limit_sentence_num)
        list_sentence_S = summa.list_sentence_S
      	message = 'クラスタ数: ' + str(local_K) + '    ' + 'γ: ' + str(local_gamma) + '    ' + 'ε: ' + str(local_epsilon) + '    ' +'λ: ' + str(local_lamda) + '    ' + 'num_sentence: ' + str(local_limit_sentence_num)
        list_S = [num + 1 for num in summa.list_S]
        list_num_sentence_S.append(zip(list_S, list_sentence_S))
        d = {
			'form': form,
            'list_sentence_V': summa.list_sentence_V,
            'list_num_sentence_S': list_num_sentence_S,
            'message': message,
        }
        return render(request, 'forms2.html', d)
    else:
        message = '要約したい文書を入力してください'
    	d = {
            'form': form,
			'list_sentence_V': [],
			'list_num_sentence_S': list_num_sentence_S,
            'message': message,
        }
        return render(request, 'forms2.html', d)
