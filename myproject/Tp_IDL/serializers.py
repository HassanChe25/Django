from rest_framework import serializers
from .models import Prtoduct , Customer ,Oreder

class PrtoductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prtoduct
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
class OrederSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oreder
        fields = '__all__'