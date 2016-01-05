# coding: utf-8
from django import forms


class InputForm(forms.Form):
    input_text = forms.CharField(
        label='テキスト',
        required=True,
		widget=forms.Textarea(attrs={'rows': 10, 'cols': 100})
    )

    K = forms.IntegerField(
        label='クラスタ数',
        min_value=0,
        max_value=200,
        required=True,
    )

    lamda = forms.CharField(
        label='ラムダ',
        required=True,
        widget=forms.TextInput(),
        initial=0.5
    )

    gamma = forms.CharField(
        label='ガンマ',
        required=True,
        widget=forms.TextInput(),
        initial=0.7
    )

    limit_sentence_num = forms.IntegerField(
        label='文の数',
        min_value=0,
        max_value=20,
        required=True,
    )


class InputForm2(forms.Form):
    input_text1 = forms.CharField(
        label='要約したい文書',
        required=True,
		widget=forms.Textarea(attrs={'rows': 10, 'cols': 100})
    )

    input_text2 = forms.CharField(
        label='比較したい文章',
        required=True,
		widget=forms.Textarea(attrs={'rows': 10, 'cols': 100})
    )

    K = forms.IntegerField(
        label='クラスタ数',
        min_value=0,
        max_value=200,
        required=True,
    )

    lamda = forms.CharField(
        label='ラムダ',
        required=True,
        widget=forms.TextInput(),
        initial=0.5
    )

    gamma = forms.CharField(
        label='ガンマ',
        required=True,
        widget=forms.TextInput(),
        initial=0.7
    )

    epsilon = forms.CharField(
        label='イプシロン',
        required=True,
        widget=forms.TextInput(),
        initial=0.5
    )

    limit_sentence_num = forms.IntegerField(
        label='文の数',
        min_value=0,
        max_value=20,
        required=True,
    )
