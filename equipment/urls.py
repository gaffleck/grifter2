from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LotsListView, CustomerListView

urlpatterns = {
    url('lots/$', LotsListView.as_view(), name="create"),
    url('customers/$', CustomerListView.as_view(), name="create"),

}

urlpatterns = format_suffix_patterns(urlpatterns)