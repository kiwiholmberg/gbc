from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gbc.views.home', name='home'),
    # url(r'^gbc/', include('gbc.foo.urls')),

    #url(r'^api/', include('core.api')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'core.views.home', name='home'),
)
