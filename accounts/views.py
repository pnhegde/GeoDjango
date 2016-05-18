from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import TransportOperator
from .serializers import TransportOperatorSerializer



class ListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_response(self, data={}):
        return Response(data, status=status.HTTP_201_CREATED)

    def get_error_response(self):
        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportOperatorMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = TransportOperator.objects.all()
    serializer_class = TransportOperatorSerializer



class TransportOperatorListCreate(TransportOperatorMixin, ListCreateAPIView):
    """
    `TransportOperatorListCreate` allows you to list all Transporters or Create a new Transporter
    """
    lookup_field = 'id'


class TransportOperatorDetail(TransportOperatorMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    `TransportOperatorDetail` allows you to get details of a TransportOperator
    or perform Update/Delete operations.
    """
    lookup_field = 'id'
