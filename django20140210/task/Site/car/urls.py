from django.conf.urls import patterns, include, url

urlpatterns = patterns('car.views',
url(r'^$', 'index'),
url(r'^new/(?P<a>.*)$', 'new'),
)
