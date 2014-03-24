from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^table/', include('table.urls', namespace='table')),
    url(r'^admin/', include(admin.site.urls)),
)
