# coding: utf-8
from django import forms

radio8 = (('1', 1), ('2', 2),
          ('3', 3), ('4', 4),
          ('5', 5), ('6', 6),
          ('7', 7), ('8', 8),
         )

radio2 = (('はい', 1), ('いいえ', 0))


class Questionnaire_exp3(forms.Form):
    user_name = forms.CharField(
            label='ユーザー名',
            required=True,
    )
    passwd = forms.CharField(
            label='passwd',
            required=False
    )
    meta2 = forms.DateField(
            label='start_time',
            required=False
    )
    meta3 = forms.DateField(
            label='end_time',
            required=False
    )

    q1_1 = forms.ChoiceField(
                label='タイプ1',
                widget=forms.RadioSelect,
                choices=radio8,
                required=True,
    )
    q1_2 = forms.ChoiceField(
                label='タイプ2',
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
                label='タイプ2',
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
                label='タイプ2',
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
                label='タイプ2',
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
                label='タイプ2',
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
                label='タイプ2',
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
                label='タイプ2',
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
    q32_1 = forms.CharField(label='タイプ1',
                            required=True,
                            widget=forms.Textarea)
    q32_2 = forms.CharField(label='タイプ2',
                            required=True,
                            widget=forms.Textarea)
    q33_1 = forms.CharField(label='タイプ1',
                            required=True,
                            widget=forms.Textarea)
    q33_2 = forms.CharField(label='タイプ2',
                            required=True,
                            widget=forms.Textarea)
