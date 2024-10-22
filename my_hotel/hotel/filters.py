from django_filters import FilterSet
from .models import Booking

class ProductFilter(FilterSet):
    class Meta:
        model = Booking
        fields = {
            'user': ['exact'],
            'room': ['exact'],
            'hotel': ['exact'],
            'check_in_date': ['exact'],
            'check_out_date': ['exact'],
            'status': ['exact'],
        }