"""API views for the HarmonizedSystemCodes plugin.

Ref: https://www.django-rest-framework.org/api-guide/views/
"""

from rest_framework import permissions

from InvenTree.filters import SEARCH_ORDER_FILTER
from InvenTree.mixins import ListCreateAPI, RetrieveUpdateDestroyAPI

from .models import HarmonizedSystemCode
from .serializers import HarmonizedSystemCodeSerializer


class HarominzedSystemCodeMixin:
    """Mixin class for the API views."""

    queryset = HarmonizedSystemCode.objects.all()
    serializer_class = HarmonizedSystemCodeSerializer

    # TODO: Adjust permissions?
    permission_classes = [permissions.IsAuthenticated]


class HarmonizedSystemCodeList(HarominzedSystemCodeMixin, ListCreateAPI):
    """API endpoint for listing or creating Harmonized System Codes."""

    filter_backends = SEARCH_ORDER_FILTER

    filterset_fields = [
        "category",
        "customer",
    ]

    ordering_fields = ["code", "category", "customer"]

    search_fields = [
        "code",
        "category__name",
        "category__description",
        "customer__name",
        "customer__description",
    ]


class HarmonizedSystemCodeDetail(HarominzedSystemCodeMixin, RetrieveUpdateDestroyAPI):
    """API endpoint for retrieving, updating, or deleting a Harmonized System Code."""

    queryset = HarmonizedSystemCode.objects.all()
    serializer_class = HarmonizedSystemCodeSerializer
