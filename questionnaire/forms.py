# coding: utf-8
from django import forms

radio8 = (('1', 1), ('2', 2),
          ('3', 3), ('4', 4),
          ('5', 5), ('6', 6),
          ('7', 7), ('8', 8),
         )

radio2 = (('はい', 1), ('いいえ', 0))


class Questionnaire1(forms.Form):
    user_name = forms.CharField(
            label='ユーザー名',
            required=True,
    )
    start_time = forms.DateField(
            label='start_time',
            input_formats=['%Y-%m-%d %h:%m:%s'],
            required=False
    )
    end_time = forms.DateField(
            label='end_time',
            input_formats=['%Y-%m-%d %h:%m:%s'],
            required=False
    )
    passwd = forms.CharField(
            label='passwd',
            required=False
    )
    q2_1 = forms.CharField(label='タイプ1', required=True, widget=forms.Textarea)
    q2_2 = forms.CharField(label='タイプ2', required=True, widget=forms.Textarea)
    q2_3 = forms.CharField(label='タイプ3', required=True, widget=forms.Textarea)
    q2_4 = forms.CharField(label='タイプ4', required=True, widget=forms.Textarea)

    q3_1 = forms.CharField(label='タイプ1', required=True, widget=forms.Textarea)
    q3_2 = forms.CharField(label='タイプ2', required=True, widget=forms.Textarea)
    q3_3 = forms.CharField(label='タイプ3', required=True, widget=forms.Textarea)
    q3_4 = forms.CharField(label='タイプ4', required=True, widget=forms.Textarea)

    q4_1 = forms.CharField(label='タイプ1', required=True, widget=forms.Textarea)
    q4_2 = forms.CharField(label='タイプ2', required=True, widget=forms.Textarea)
    q4_3 = forms.CharField(label='タイプ3', required=True, widget=forms.Textarea)
    q4_4 = forms.CharField(label='タイプ4', required=True, widget=forms.Textarea)

    q5 = forms.CharField(required=True, widget=forms.Textarea)

    q6 = forms.CharField(required=True, widget=forms.Textarea)

    q7_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q7_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    
    q7_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q7_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q8_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q8_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q8_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q8_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q9_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q9_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q9_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q9_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q10_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q10_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q10_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q10_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q11_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q11_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q11_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q11_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q12_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q12_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q12_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q12_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q13_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q13_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q13_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q13_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q14_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q14_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q14_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q14_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q15_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q15_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q15_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q15_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q16_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q16_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q16_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q16_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q17_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q17_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q17_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q17_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q18_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q18_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q18_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q18_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q19_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q19_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q19_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q19_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q20_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q20_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q20_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q20_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q21_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q21_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q21_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q21_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q22_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q22_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q22_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q22_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q23_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q23_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q23_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q23_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q24_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q24_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q24_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q24_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q25_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q25_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q25_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q25_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q26_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q26_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q26_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q26_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q27_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q27_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q27_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q27_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q28_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q28_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q28_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q28_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q29_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q29_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q29_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q29_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q30_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q30_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q30_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q30_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q31_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q31_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q31_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q31_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q32_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q32_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q32_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q32_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q33_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q33_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q33_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q33_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q34_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q34_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q34_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q34_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q35_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q35_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q35_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q35_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q36_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q36_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q36_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q36_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q37_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q37_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q37_3 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q37_4 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )


class Questionnaire2(forms.Form):
    user_name = forms.CharField(
            label='ユーザー名',
            required=True,
    )
    passwd = forms.CharField(
            label='passwd',
            required=False
    )

    q1_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q1_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    
    q2_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q2_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q3_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q3_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q4_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q4_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q5_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q5_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q6_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q6_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q7_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q7_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q8_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q8_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q9_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q9_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q10_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q10_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q11_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q11_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q12_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q12_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q13_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q13_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q14_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q14_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q15_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q15_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q16_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q16_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q17_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q17_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q18_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q18_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q19_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q19_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q20_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q20_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q21_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q21_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q22_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q22_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q23_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q23_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q24_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q24_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q25_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q25_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q26_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q26_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q27_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q27_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q28_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q28_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q29_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q29_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q30_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q30_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q31_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q31_2 = forms.ChoiceField(
                label='タイプ4',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q32_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q32_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    
    q33_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q33_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q34_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q34_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q35_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q35_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q36_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q36_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q37_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q37_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q38_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q38_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q39_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q39_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q40_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q40_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q41_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q41_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q42_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q42_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q43_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q43_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q44_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q44_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q45_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q45_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q46_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q46_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q47_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q47_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q48_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q48_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q49_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q49_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q50_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q50_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q51_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q51_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q52_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q52_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q53_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q53_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q54_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q54_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q55_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q55_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q56_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q56_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q57_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q57_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q58_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q58_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q59_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q59_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q60_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q60_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q61_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q61_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q62_1 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q62_2 = forms.ChoiceField(
                label='タイプ3',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )


class Questionnaire_exp2(forms.Form):
    question1 = forms.CharField(
            label='question1',
            required=True,
    )
    meta1 = forms.CharField(
            label='type',
            required=True,
    )
    meta2 = forms.DateField(
            label='start_time',
            input_formats=['%Y-%m-%d %h:%m:%s'],
            required=False
    )
    meta3 = forms.DateField(
            label='end_time',
            input_formats=['%Y-%m-%d %h:%m:%s'],
            required=False
    )
    passwd = forms.CharField(
            label='passwd',
            required=False
    )
    q2 = forms.ChoiceField(
                label='question2',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q2 = forms.ChoiceField(
                label='question2',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q2 = forms.ChoiceField(
                label='question2',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q2 = forms.ChoiceField(
                label='question2',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q2 = forms.ChoiceField(
                label='question2',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q2_1 = forms.CharField(label='タイプ1', required=True, widget=forms.Textarea)
    q2_2 = forms.CharField(label='タイプ2', required=True, widget=forms.Textarea)
    q2_3 = forms.CharField(label='タイプ3', required=True, widget=forms.Textarea)
    q2_4 = forms.CharField(label='タイプ4', required=True, widget=forms.Textarea)

    q3_1 = forms.CharField(label='タイプ1', required=True, widget=forms.Textarea)
    q3_2 = forms.CharField(label='タイプ2', required=True, widget=forms.Textarea)
    q3_3 = forms.CharField(label='タイプ3', required=True, widget=forms.Textarea)
    q3_4 = forms.CharField(label='タイプ4', required=True, widget=forms.Textarea)

    q4_1 = forms.CharField(label='タイプ1', required=True, widget=forms.Textarea)
    q4_2 = forms.CharField(label='タイプ2', required=True, widget=forms.Textarea)
    q4_3 = forms.CharField(label='タイプ3', required=True, widget=forms.Textarea)
    q4_4 = forms.CharField(label='タイプ4', required=True, widget=forms.Textarea)

    q5 = forms.CharField(required=True, widget=forms.Textarea)

    q6 = forms.CharField(required=True, widget=forms.Textarea)

    q7_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

    q7_2 = forms.ChoiceField(
                label='タイプ2',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )

