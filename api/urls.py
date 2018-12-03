# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomerCreateView, CustomerDetailsView, FriendCreateView, FriendDetailsView, schema_view

urlpatterns = {
    url('customers/$', CustomerCreateView.as_view(), name="create"),
    url('customers/(?P<pk>[0-9]+)/$',
        CustomerDetailsView.as_view(), name="details"),
    url('friends/$', FriendCreateView.as_view(), name="create"),
    url('friends/(?P<pk>[0-9]+)/$',
        FriendDetailsView.as_view(), name="details"),
    
    
}

urlpatterns = format_suffix_patterns(urlpatterns)