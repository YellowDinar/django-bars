from django.conf.urls import patterns, include, url

urlpatterns = patterns('groups.views',
    url(r'^$', 'index'),
    url(r'^(?P<id>\d+)$', 'details'),
)
