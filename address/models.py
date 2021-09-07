from django.db import models


class Address(models.Model):
    """
    Object that represents an Address.
    """
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state}, {self.postcode}, {self.country}'
