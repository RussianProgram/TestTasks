from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import OfferSerialiser
from .models import Offer

class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerialiser
    queryset = Offer.objects.all()


