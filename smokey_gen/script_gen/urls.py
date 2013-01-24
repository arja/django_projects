from django.conf.urls import patterns, url

from script_gen import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name='index'),
    url(r'^testlist/', views.showTestList, name='showTestList'),
    url(r'^/generate/', views.generateScript, name='generateScript'),
    url(r'^/addtest/', views.addTest, name='addTest'),
    url(r'^/deletetest/(?P<testid>\d+)', views.deleteTest, name='deleteTest'),
)
