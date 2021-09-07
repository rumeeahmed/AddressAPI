from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    """
    Object that serializes data for the Address Model.
    """
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'postcode', 'country']
