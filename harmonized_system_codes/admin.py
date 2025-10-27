"""Admin site configuration for the HarmonizedSystemCodes plugin."""

from django.contrib import admin

from .models import HarmonizedSystemCode


@admin.register(HarmonizedSystemCode)
class HarmonizedSystemCodeAdmin(admin.ModelAdmin):
    """Admin interface for the HarmonizedSystemCode."""

    list_display = (
        "code",
        "category",
    )

    autocomplete_fields = (
        "category",
        "customer",
    )
