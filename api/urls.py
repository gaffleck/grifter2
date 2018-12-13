# api/urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserCreateView, UserDetailsView, ContactCreateView, \
ContactDetailsView

urlpatterns = {
    url('user/$', UserCreateView.as_view(), name="create"),
    url('users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="details"),
    url('contacts/$', ContactCreateView.as_view(), name="create"),
    url('contacts/(?P<pk>[0-9]+)/$',
        ContactDetailsView.as_view(), name="details")
    
}

urlpatterns = format_suffix_patterns(urlpatterns)