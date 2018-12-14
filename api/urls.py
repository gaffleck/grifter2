# api/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserCreateView, UserDetailsView , ContactCreateView,\
ContactDetailsView, NoteCreateView, NoteDetailsView, AssetCreateView, AssetDetailsView,\
PurchaseCreateView, PurchaseDetailsView, ConversationCreateView, ConversationDetailsView,\
MessageCreateView, MessageDetailsView, TwilioReplyCreateView, \
TwilioReplyDetailsView, TwilioMessageCreateView, TwilioMessageDetailsView, ImageDetailsView, \
ImageCreateView


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
        PurchaseDetailsView.as_view(), name="details"),
    url('conversations/$', ConversationCreateView.as_view(), name="create"),
    url('conversations/(?P<pk>[0-9]+)/$',
        ConversationDetailsView.as_view(), name="details"),
    url('messages/$', MessageCreateView.as_view(), name="create"),
    url('messages/(?P<pk>[0-9]+)/$',
        MessageDetailsView.as_view(), name="details"), 
    url('images/$', ImageCreateView.as_view(), name="create"),
    url('images/(?P<pk>[0-9]+)/$',
        ImageDetailsView.as_view(), name="details"), 
    url('twilioReplies/$', TwilioReplyCreateView.as_view(), name="create"),
    url('twilioReplies/(?P<pk>[0-9]+)/$',
        TwilioReplyDetailsView.as_view(), name="details"),
    url('twilioMessages/$', TwilioMessageCreateView.as_view(), name="create"),
    url('twilioMessages/(?P<pk>[0-9]+)/$',
        TwilioMessageDetailsView.as_view(), name="details"),


}

urlpatterns = format_suffix_patterns(urlpatterns)