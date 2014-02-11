from django.conf.urls import patterns, include, url

#

urlpatterns = patterns('math2.views',

url(r'^$', 'index'),
url(r'^(?P<a>\d+)/(?P<b>\d+)$', 'add'),
)
