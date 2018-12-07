# api/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserCreateView, UserDetailsView, ContactCreateView, \
ContactDetailsView, GiftRecordCreateView, GiftRecordDetailsView, GiftCreateView, \
GiftDetailsView, GiftSuggestionDetailsView, GiftSuggestionCreateView, SpecialDateTypeCreateView,\
SpecialDateTypeDetailsView, SpecialDateCreateView, SpecialDateDetailsView

urlpatterns = {
    url('user/$', UserCreateView.as_view(), name="create"),
    url('users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="details"),
    url('contacts/$', ContactCreateView.as_view(), name="create"),
    url('contacts/(?P<pk>[0-9]+)/$',
        ContactDetailsView.as_view(), name="details"),
    url('giftRecords/$', GiftRecordCreateView.as_view(), name="create"),
    url('giftRecords/(?P<pk>[0-9]+)/$',
        GiftRecordDetailsView.as_view(), name="details"),
    url('gifts/$', GiftCreateView.as_view(), name="create"),
    url('gifts/(?P<pk>[0-9]+)/$',
        GiftDetailsView.as_view(), name="details"),
    url('giftSuggestions/$', GiftSuggestionCreateView.as_view(), name="create"),
    url('giftSuggestions/(?P<pk>[0-9]+)/$',
        GiftSuggestionDetailsView.as_view(), name="details"),
    url('specialDateTypes/$', SpecialDateTypeCreateView.as_view(), name="create"),
    url('specialDateTypes/(?P<pk>[0-9]+)/$',
        SpecialDateTypeDetailsView.as_view(), name="details"),
    url('specialDate/$', SpecialDateCreateView.as_view(), name="create"),
    url('specialDate/(?P<pk>[0-9]+)/$',
        SpecialDateDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)