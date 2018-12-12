import django_filters.rest_framework
from rest_framework import generics
from .serializers import LotSerializer, CustomerSerializer, SaleSerializer
from .models import Lot, Customer, Sale

class LotsListView(generics.ListAPIView):
    """ Lot List View"""
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Lot.objects.all()
        lot = self.request.query_params.get('lot_num', None)
        if lot is not None:
            queryset = queryset.filter(lot_num=lot)
        return queryset

class CustomerListView(generics.ListAPIView):
    """ Lot List View"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SaleListView(generics.ListAPIView):
    """ Lot List View"""
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
