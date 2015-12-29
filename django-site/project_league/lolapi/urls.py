from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /lol/
    # ex: /lol/5/
    url(r'^(?P<summoner_name>.+)/$', views.detail, name='detail'),
]
