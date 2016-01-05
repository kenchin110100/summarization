from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='hoem'),
    url(r'^get/$', views.hello_get_query, name='hello_get_query'),
    url(r'^forms/$', views.hello_forms, name='hello_forms'),
    url(r'^summarize/$', views.summarize, name='summarize'),
    url(r'^summarize2/$', views.summarize2, name='summarize2'),
]
