from django.conf.urls import patterns, url

from script_gen import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^script_gen/add/', views.addTest, name='addTest')
)
