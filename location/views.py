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
    """
    `PolygonAddressFilter` is used for filtering geo points in a Polygon
    """
    def filter_queryset(self, request, queryset, view):
        latlng = request.query_params.get('contains')
        if not latlng:
            return queryset
        latlng = map(float, latlng.split(','))
        ##TODO: Handle exections
        return queryset.filter(latlng__bbcontains=Point(latlng))


class PolygonAddressListCreate(PolygonAddressMixin, ListCreateAPIView):
    """
    `PolygonAddressListCreate` API allows you to create a new polygon or List all existing polygons.
    Example Input:
    {
        "latlng": {"type":"Polygon","coordinates": [[ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]] ]},
        "name": "Polygon Name",
        "price": "1010"
    }
    """
    filter_fields = ('latlng',)
    filter_backends = (PolygonAddressFilter, )

    def get_queryset(self):
        return PolygonAddress.objects.filter(operator=self.request.user)



class PolygonAddressDetail(PolygonAddressMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    `PolygonAddressDetail` allows you to get, update and delete a particual PolygonAddress.
    """
    lookup_field = 'id'

