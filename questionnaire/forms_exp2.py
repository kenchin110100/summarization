# coding: utf-8
from django import forms

radio8 = ((1, 1), (2, 2),
          (3, 3), (4, 4),
          (5, 5), (6, 6),
          (7, 7), (8, 8),
         )

radio2 = ((1, 'はい'), (0, 'いいえ'))
radio_sens2 = ((3, '人よりも先に新しい商品やサービスを利用したり、新しいお店に行くほうである'),
		       (2, '少し様子をみてから、新しい商品やサービスを利用したり、新しいお店に行くほうである'),
		       (1, '一般に普及してから、新しい商品やサービスを利用したり、新しいお店に行くほうである'),
			   (0, '新しい商品やサービス、お店には関心がないほうである'))
radio_pi = ((3, 'ぜひ利用したい'),
		    (2, '利用したい'),
		    (1, 'どちらでもない'),
			(0, '利用したくない'))
radio_hotel = ((0 ,'ホテルA'), (1, 'ホテルB'), (2 ,'ホテルC'), (3, 'ホテルD'))
radio6 = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6))


class Questionnaire_exp2(forms.Form):
    q1 = forms.CharField(
            label='user_name',
            required=True,
    )
    meta1 = forms.CharField(
            label='type',
            required=False,
    )
    meta2 = forms.DateTimeField(
            label='start_time',
            required=False
    )
    meta3 = forms.DateTimeField(
            label='end_time',
            required=False
    )
    passwd = forms.CharField(
            label='passwd',
            required=False
    )
    q2 = forms.ChoiceField(
                label='Q2',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q3 = forms.ChoiceField(
                label='Q3',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q4 = forms.ChoiceField(
                label='Q4',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q5 = forms.ChoiceField(
                label='Q5',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q6 = forms.ChoiceField(
                label='Q6',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q7 = forms.ChoiceField(
                label='Q7',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q8 = forms.ChoiceField(
                label='Q8',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q9 = forms.ChoiceField(
                label='Q9',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q10 = forms.ChoiceField(
                label='Q10',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q11 = forms.ChoiceField(
                label='Q11',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q12 = forms.ChoiceField(
                label='Q12',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q13 = forms.ChoiceField(
                label='Q13',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q14 = forms.ChoiceField(
                label='Q14',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q15 = forms.ChoiceField(
                label='Q15',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q16 = forms.ChoiceField(
                label='Q16',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q17 = forms.ChoiceField(
                label='Q17',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q18 = forms.ChoiceField(
                label='Q18',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q19 = forms.ChoiceField(
                label='Q19',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q20 = forms.ChoiceField(
                label='Q20',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q21 = forms.ChoiceField(
                label='Q21',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q22 = forms.ChoiceField(
                label='Q22',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q23 = forms.ChoiceField(
                label='Q23',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q24 = forms.ChoiceField(
                label='Q24',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q25 = forms.ChoiceField(
                label='Q25',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q26 = forms.ChoiceField(
                label='Q26',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q27 = forms.ChoiceField(
                label='Q27',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q28 = forms.ChoiceField(
                label='Q28',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q29 = forms.ChoiceField(
                label='Q29',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q30 = forms.ChoiceField(
                label='Q30',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q31 = forms.ChoiceField(
                label='Q31',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q32 = forms.ChoiceField(
                label='Q32',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q33 = forms.ChoiceField(
                label='Q33',
                widget=forms.RadioSelect,
                choices=radio2,
                required=True,
    )
    q35 = forms.ChoiceField(
                label='Q35',
                widget=forms.RadioSelect,
                choices=radio_sens2,
                required=True,
    )
    q36_1 = forms.ChoiceField(
                label='Q36_1',
                widget=forms.RadioSelect,
                choices=radio_pi,
                required=True,
    )
    q36_2 = forms.CharField(label='Q36_2', required=True, widget=forms.Textarea)
    q37_1 = forms.ChoiceField(
                label='Q37_1',
                widget=forms.RadioSelect,
                choices=radio_pi,
                required=True,
    )
    q37_2 = forms.CharField(label='Q37_2', required=True, widget=forms.Textarea)
    q38_1 = forms.ChoiceField(
                label='Q38_1',
                widget=forms.RadioSelect,
                choices=radio_pi,
                required=True,
    )
    q38_2 = forms.CharField(label='Q38_2', required=True, widget=forms.Textarea)
    q39_1 = forms.ChoiceField(
                label='Q39_1',
                widget=forms.RadioSelect,
                choices=radio_pi,
                required=True,
    )
    q39_2 = forms.CharField(label='Q39_2', required=True, widget=forms.Textarea)
    q40 = forms.ChoiceField(
                label='Q40',
                widget=forms.RadioSelect,
                choices=radio_hotel,
                required=True,
    )
    q41 = forms.ChoiceField(
                label='Q41',
                widget=forms.RadioSelect,
                choices=radio_hotel,
                required=True,
    )
    q42_1 = forms.ChoiceField(
                label='Q42_1',
                widget=forms.RadioSelect,
                choices=radio6,
                required=True,
    )
    q42_2 = forms.ChoiceField(
                label='Q42_2',
                widget=forms.RadioSelect,
                choices=radio6,
                required=False,
    )
    q42_3 = forms.ChoiceField(
                label='Q42_3',
                widget=forms.RadioSelect,
                choices=radio6,
                required=True,
    )
