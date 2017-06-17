from django.conf.urls import url
from . import views, views_exp2, views_exp3

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index1$', views.index1, name='index1'),
    url(r'^index2$', views.index2, name='index2'),
    url(r'^questionnaire1$', views.questionnaire1, name='questionnaire1'),
    url(r'^questionnaire2$', views.questionnaire2, name='questionnaire2'),
    url(r'^review1$', views.review1, name='review1'),
    url(r'^review$', views.review, name='review'),
    url(r'^review_exp2_1$', views_exp2.review_exp2_1, name='review_exp2_1'),
    url(r'^review_exp2_2$', views_exp2.review_exp2_2, name='review_exp2_2'),
    url(r'^questionnaire_exp2_1$', views_exp2.questionnaire_exp2_1, name='questionnaire_exp2_1'),
    url(r'^questionnaire_exp2_2$', views_exp2.questionnaire_exp2_2, name='questionnaire_exp2_2'),
    url(r'^index_exp2$', views_exp2.index_exp2, name='index_exp2'),
    url(r'^consent_exp2$', views_exp2.consent_exp2, name='consent'),
    url(r'^review_exp3$', views_exp3.review_exp3, name='review_exp3'),
    url(r'^questionnaire_exp3$', views_exp3.questionnaire_exp3, name='questionnaire_exp3'),
    url(r'^index_exp3$', views_exp3.index_exp3, name='index_exp3'),
    url(r'^consent_exp3$', views_exp3.consent_exp3, name='consent'),
    # url(r'^consent$', views.consent, name='consent'),
]
