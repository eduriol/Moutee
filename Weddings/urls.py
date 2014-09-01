from django.conf.urls import patterns, url

from Weddings import views

urlpatterns = patterns('',
    # ex: /weddings/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /weddings/5/
    url(r'^(?P<wedding_id>\d+)/$', views.detail, name='detail'),
    # ex: /weddings/5/add_guest/
    #url(r'^(?P<wedding_id>\d+)/add_guest/$', views.add_guest, name='add_guest'),
    # ex: /weddings/5/guest_detail/4/
    url(r'^(?P<wedding_id>\d+)/guest/(?P<guest_id>\d+)$', views.guest, name='guest'),
)