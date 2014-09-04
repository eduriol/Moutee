from django.conf.urls import patterns, url

from Weddings import views

urlpatterns = patterns('',
    # ex: /weddings/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /weddings/5/
    url(r'^(?P<wedding_id>\d+)/$', views.detail, name='detail'),
    # ex: /weddings/5/guest/4/
    url(r'^(?P<wedding_id>\d+)/guest/(?P<guest_id>\d+)$', views.guest, name='guest'),
)