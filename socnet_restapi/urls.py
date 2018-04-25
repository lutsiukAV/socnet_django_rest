"""socnet_restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
from socnet.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

api_urls = [
    url(r'^users/$', UserHandler.as_view()),
    url(r'^posts/$', PostHandler.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),
    url(r'^likes/(?P<pk>[0-9]+)/$', LikesHandler.as_view()),
    url(r'^auth/$', views.obtain_auth_token),
]

api_urls = format_suffix_patterns(api_urls)
urlpatterns += api_urls