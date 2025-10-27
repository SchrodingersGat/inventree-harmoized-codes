"""Custom template tags for the HarmonizedSystemCodes plugin."""

from django import template

register = template.Library()


@register.simple_tag
def harmonized_code(part, customer=None):
    """Retrieve the Harmonized System Code for a given part and optional company."""
    from ..helpers import get_harmonized_code

    return get_harmonized_code(part, customer)
