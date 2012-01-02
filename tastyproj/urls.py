from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from myapp.api import v1_api

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tastyproj.views.home', name='home'),
    # url(r'^tastyproj/', include('tastyproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls))
)
