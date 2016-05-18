from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models  import TransportOperator


class TransportOperatorSerializer(serializers.ModelSerializer):
    """
    `TransportOperatorSerializer` serializes the TransportOperator object.
    """
    class Meta:
        model = TransportOperator
        fields = (
            'email', 'name',  'phone',
            'language', 'currency'
        )
