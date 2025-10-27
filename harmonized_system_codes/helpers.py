"""Helper function for the HarmonizedSystemCodes plugin."""

from .models import HarmonizedSystemCode


def get_harmonized_code(part, customer=None) -> HarmonizedSystemCode:
    """Retrieve the harmonized system code for a given part and optional customer.

    Arguments:
        part: The part instance for which to retrieve the HS code.
        customer: (Optional) The company instance to filter the HS code by customer.

    Returns:
        HarmonizedSystemCode instance if found, else None.
    """

    category = part.category

    # No category, no code
    if not category:
        return None

    # Work up the category tree to find a matching code
    categories = category.get_ancestors(include_self=True)

    hs_codes = HarmonizedSystemCode.objects.filter(category__in=categories)

    # Order by category level (deepest level first)
    hs_codes = hs_codes.order_by("-category__level")

    # First, try matching against a Company (if provided)
    # A company-specific code will override a generic one
    if customer:
        company_hs_codes = hs_codes.filter(customer=customer)
        if company_hs_codes.exists():
            return company_hs_codes.first()

    # Return the first matching code, or None if not found
    return hs_codes.first()
