from rest_framework import  serializers
from .models import Employee,Address

class EmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Address
        fields = '__all__'