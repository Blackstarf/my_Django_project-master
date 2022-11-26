
from rest_framework import viewsets

from lms.models import Curator
from lms.serializer import CuratorSerializer


class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = CuratorSerializer
