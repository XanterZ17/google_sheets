from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import Test
from .serializers import TestSerializer

# Create your views here.
class GetTestTable(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer