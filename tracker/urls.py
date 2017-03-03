from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'login/$', views.login_page, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^settings/$', views.edit_tracker, name='edit'),
]
