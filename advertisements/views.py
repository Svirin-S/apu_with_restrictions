from django_filters import FilterSet, DateTimeFromToRangeFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Adv
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvSerializer
from .filters import Filter


class AdvModelViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_class = Filter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
