from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'moviesApp.views.index', name='index'),
    url(r'^moviesApp/', include('moviesApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
