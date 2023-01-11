from django_filters import FilterSet, DateTimeFromToRangeFilter
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Adv
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvSerializer


class AdvModelViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsOwner]
    filterset_fields = ['open']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


