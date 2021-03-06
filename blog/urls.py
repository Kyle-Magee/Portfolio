"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^resume/', include('resume.urls')),
    url(r'^',  include('posts.urls'), name='posts'),
    url(r'^gsm/', include('gsm.urls'), name='gsm'),
    url(r'^tracker/', include('tracker.urls'), name='tracker'),
    url(r'mathsuccesscenter/', include('mathsuccesscenter.urls'),
        name='mathsuccesscenter'),
    url(r'river_simulation/', include('river_simulation.urls'),
        name='river_simulation')
]
