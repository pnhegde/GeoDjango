
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models  import PolygonAddress, CustomPolygonField
from accounts.models import TransportOperator
from GeoDjango import utils


class PolygonAddressSerializer(GeoFeatureModelSerializer):
    """
    """
    operator = serializers.SlugRelatedField( queryset=TransportOperator.objects.all(),
        default=serializers.CurrentUserDefault(), slug_field = 'name'
    )
    latlng = CustomPolygonField()
    class Meta:
        model = PolygonAddress
        geo_field = 'latlng'

