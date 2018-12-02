# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomerCreateView, CustomerDetailsView

urlpatterns = {
    url('customers/$', CustomerCreateView.as_view(), name="create"),
    url('customers/(?P<pk>[0-9]+)/$',
        CustomerDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)