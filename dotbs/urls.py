from django.conf.urls import patterns, include, url
from django.contrib import admin

from dotbs import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^analyze/', views.analyze, name='analyze'),

    url(r'^admin/', include(admin.site.urls)),
)
