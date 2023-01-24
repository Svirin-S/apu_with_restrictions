from django_filters import FilterSet, DateTimeFromToRangeFilter, BooleanFilter

from .models import Adv


class Filter(FilterSet):
    created_at = DateTimeFromToRangeFilter()
    open = BooleanFilter

    class Meta:
        model = Adv
        fields = ['created_at', 'open']