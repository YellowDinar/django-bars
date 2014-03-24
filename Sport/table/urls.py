from django.conf.urls import patterns,url

urlpatterns = patterns('table.views',
                       url(r'^$', 'index', name='index'),
)