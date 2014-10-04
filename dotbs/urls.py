from django.conf.urls import patterns, include, url
from django.contrib import admin

from dotbs import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
