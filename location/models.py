from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models  as gsmodels
from rest_framework_gis.fields import GeometryField
from django.contrib.gis.geos import Polygon, GEOSGeometry, GEOSException
from django.contrib.gis.gdal import OGRException
from django.core.exceptions import ValidationError
from accounts.models import TransportOperator


class CustomPolygonField(GeometryField):
    """
    `CustomPolygonField` is used for serializing GeoJson data while creating PolygonAddress.
    """
    type_name = 'CustomPolygonField'

    def to_internal_value(self, value):
        if value == '' or value is None:
            return value
        if isinstance(value, GEOSGeometry):
            return value
        if isinstance(value, dict):
            if value['type'] == "Polygon":
                colist = value['coordinates']
                for i in colist:
                    value = tuple(tuple(x) for x in i)
                return GEOSGeometry(Polygon((value)))
            else:
                raise ValidationError(_('Invalid format: Polygon JSON expected'))
        try:
            return GEOSGeometry(value)
        except (ValueError, GEOSException, OGRException, TypeError):
            raise ValidationError(('Invalid format: string or unicode input unrecognized as GeoJSON, WKT EWKT or HEXEWKB.'))


class PolygonAddress(models.Model):
    """
    `PolygonAddress` stores Polygon in PostGIS.
    """
    name = models.CharField(max_length=64, null=False, blank=True)
    operator = models.ForeignKey(TransportOperator)
    price = models.CharField(max_length=64, null=True, blank=True)
    latlng = gsmodels.GeometryField()
    objects = gsmodels.GeoManager()
