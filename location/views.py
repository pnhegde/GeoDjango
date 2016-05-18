from accounts.views import ListCreateAPIView
from rest_framework import filters, generics

from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis import filters as gisfilters
from django.contrib.gis.geos import Point

from .models import PolygonAddress
from .serializers import PolygonAddressSerializer


class PolygonAddressMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = PolygonAddress.objects.all()
    serializer_class = PolygonAddressSerializer


class PolygonAddressFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        latlng = request.query_params.get('contains')
        if not latlng:
            return queryset
        latlng = map(float, latlng.split(','))
        ##TODO: Handle exections
        return queryset.filter(latlng__bbcontains=Point(latlng))


class PolygonAddressListCreate(PolygonAddressMixin, ListCreateAPIView):
    filter_fields = ('latlng',)
    filter_backends = (PolygonAddressFilter, )

    # def post(self, request, *args, **kwargs):



class PolygonAddressDetail(PolygonAddressMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'

