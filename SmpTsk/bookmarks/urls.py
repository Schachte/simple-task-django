"""bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import include, url
from bkmks.views import deleter, main_page, profile_page, user_login, profile_overview, adder, task_submission,register
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.conf import settings


urlpatterns = [

	url(r'^$', main_page, name = 'home'),
	url(r'^static(?P<path>.*)$', 'django.views.static.serve', {
	'document_root': settings.STATIC_ROOT}),
	url(r'^login/$', user_login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
          url(r'^logout/$', 'django.contrib.auth.views.logout',
          {
            "next_page" : reverse_lazy('login')
          }, name="logout"),
    url(r'^user/(\w+)/$', profile_page, name='profile'),
    url(r'^user/(\w+)/overview/$', profile_overview, name='overview'),
    url(r'^user/(\w+)/add/$',adder , name='overview'),
    url(r'^user/(\w+)/delete/(\d+)/$', deleter),
    url(r'^user/(\w+)/submitted/$', task_submission, name='submitted'),
    url(r'^register/$', register, name='register'),
]

