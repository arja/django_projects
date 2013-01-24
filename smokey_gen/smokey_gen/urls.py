from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#import script_gen
#from script_gen import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smokey_gen.views.home', name='home'),
    # url(r'^smokey_gen/', include('smokey_gen.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^script_gen/', include('script_gen.urls')),
#   url(r'^script_gen/index$', script_gen.views.index),
#   url(r'^script_gen/add/$', script_gen.views.addTest),
#   url(r'^script_gen/testlist/$', script_gen.views.showTestList),
#   url(r'^script_gen/delete/$', script_gen.views.deleteTest),
#   url(r'^script_gen/testlist/generate/$', script_gen.views.generateScript)
)
