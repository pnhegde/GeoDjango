from __future__ import unicode_literals

from django.db import models
from custom_user.models import AbstractEmailUser
from django.utils import timezone as django_timezone

LANGUAGE_CHOICES = (
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('kannada', 'Kannada'),
        ('tamil', 'Tamil'),
        ('telugu', 'Telugu'),
        ('malayalam', 'Malayalam'),
        ('marathi', 'Marathi'),
        ('bengali', 'Bengali'),
        ('gujarathi', 'Gujarathi')
        #  add as needed
    )

CURRENCY = (
    ('USD', 'US Dollar'),
    ('INR', 'Indian Rupees'),
)


class TransportOperator(AbstractEmailUser):
    """
    `TransportOperator` is a Django user who provides Transportation services and managers `PolygonAddress`.
    """
    name = models.CharField(max_length=128, null=False, blank=True)
    phone = models.CharField(max_length=32, null=False, blank=True)
    language = models.CharField(max_length=200, null=False, default='english',
        choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY) # You can make use of django-money instead.
    timezone = models.CharField(max_length=64, null=False, default='UTC')

    def __unicode__(self):
        return self.email
