from django.db import models

from django.contrib.auth.models import User
from django_filters import FilterSet, DateTimeFromToRangeFilter


class Adv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)


class F(FilterSet):
    created_at = DateTimeFromToRangeFilter()

    class Meta:
        model = Adv
        fields = ['created_at']






