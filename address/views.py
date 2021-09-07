from rest_framework import generics, permissions
from .serializers import AddressSerializer
from .models import Address


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer
