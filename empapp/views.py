from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import ModelViewSet
from .serializers import EmpSerializer,AddressSerializer
from .models import Employee,Address

class EmpViewSet(ModelViewSet):
    serializer_class = EmpSerializer
    queryset = Employee.objects.all()


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()