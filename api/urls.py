# api/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomerCreateView, CustomerDetailsView, FriendCreateView, \
FriendDetailsView, GiftRecordCreateView, GiftRecordDetailsView, GiftCreateView, \
GiftDetailsView, GiftSuggestionDetailsView, GiftSuggestionCreateView, SpecialDateTypeCreateView,\
SpecialDateTypeDetailsView, SpecialDateCreateView, SpecialDateDetailsView

urlpatterns = {
    url('customers/$', CustomerCreateView.as_view(), name="create"),
    url('customers/(?P<pk>[0-9]+)/$',
        CustomerDetailsView.as_view(), name="details"),
    url('friends/$', FriendCreateView.as_view(), name="create"),
    url('friends/(?P<pk>[0-9]+)/$',
        FriendDetailsView.as_view(), name="details"),
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