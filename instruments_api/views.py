from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import InstrumentSerializer
from .models import Instrument

# /Instruments POST GET
class InstrumentList(generics.ListCreateAPIView):
    queryset = Instrument.objects.all().order_by('id')
    serializer_class = InstrumentSerializer

# /Instruments/<id> GET PUT DELETE
class InstrumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instrument.objects.all().order_by('id')
    serializer_class = InstrumentSerializer