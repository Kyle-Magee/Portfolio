from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^river_sim.py', views.river),
]