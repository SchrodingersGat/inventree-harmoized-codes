"""Custom model definitions for the HarmonizedSystemCodes plugin.

This file is where you can define any custom database models.

- Any models defined here will require database migrations to be created.
- Don't forget to register your models in the admin interface if needed!
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from part.models import PartCategory
from company.models import Company


class HarmonizedSystemCode(models.Model):
    """Model representing a Harmonized System Code."""

    class Meta:
        """Meta options for the model."""

        app_label = "harmonized_system_codes"
        verbose_name = _("Harmonized System Code")
        verbose_name_plural = _("Harmonized System Codes")

    code = models.CharField(
        max_length=20,
        verbose_name=_("Code"),
        help_text=_("Harmonized System Code"),
    )

    description = models.CharField(
        max_length=250,
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Description of the Harmonized System Code"),
    )

    category = models.ForeignKey(
        PartCategory,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        help_text=_("Part category associated with this HS code"),
        related_name="hs_codes",
    )

    customer = models.ForeignKey(
        Company,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Customer"),
        help_text=_("Customer associated with this HS code"),
        related_name="hs_codes",
    )

    notes = models.CharField(
        max_length=500,
        blank=True,
        verbose_name=_("Notes"),
        help_text=_("Additional notes about the HS code"),
    )
