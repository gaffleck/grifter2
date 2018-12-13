# api/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserCreateView, UserDetailsView , ContactCreateView,\
ContactDetailsView, NoteCreateView, NoteDetailsView, AssetCreateView, AssetDetailsView,\
PurchaseCreateView, PurchaseDetailsView


urlpatterns = {
    url('user/$', UserCreateView.as_view(), name="create"),
    url('users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="details"),
    url('contacts/$', ContactCreateView.as_view(), name="create"),
    url('contacts/(?P<pk>[0-9]+)/$',
        ContactDetailsView.as_view(), name="details"),
    url('notes/$', NoteCreateView.as_view(), name="create"),
    url('notes/(?P<pk>[0-9]+)/$',
        NoteDetailsView.as_view(), name="details"),
    url('assets/$', AssetCreateView.as_view(), name="create"),
    url('assets/(?P<pk>[0-9]+)/$',
        AssetDetailsView.as_view(), name="details"),
    url('purchases/$', PurchaseCreateView.as_view(), name="create"),
    url('purchases/(?P<pk>[0-9]+)/$',
        PurchaseDetailsView.as_view(), name="details")


}

urlpatterns = format_suffix_patterns(urlpatterns)