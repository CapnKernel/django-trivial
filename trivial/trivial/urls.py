from django.conf.urls import patterns, include, url
from django.shortcuts import render

urlpatterns = patterns('',
    url(r'^$', lambda request: render(request, 'page.html')),
)
