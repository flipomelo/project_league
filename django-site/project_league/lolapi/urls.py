from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /lol/
    url(r'^$', views.index, name='index'),
    # ex: /lol/5/
    url(r'^(?P<summoner_name>\w)/$', views.detail, name='detail'),
]
