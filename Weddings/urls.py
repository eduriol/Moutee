from django.conf.urls import patterns, url

from Weddings import views

urlpatterns = patterns('',
    # ex: /weddings/
    url(r'^$', views.index, name='index'),
    # ex: /weddings/5/
    url(r'^(?P<wedding_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<wedding_id>\d+)/add_guest/$', views.add_guest, name='add_guest'),
)