from django.urls import path
from address.views import AddressList, AddressDetail

urlpatterns = [
    path('address/', AddressList.as_view()),
    path('books/<int:id>', AddressDetail.as_view()),
]
