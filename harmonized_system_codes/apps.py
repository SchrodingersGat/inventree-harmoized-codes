"""Django config for the HarmonizedSystemCodes plugin."""

from django.apps import AppConfig


class HarmonizedSystemCodesConfig(AppConfig):
    """Config class for the HarmonizedSystemCodes plugin."""

    name = "harmonized_system_codes"

    def ready(self):
        """This function is called whenever the HarmonizedSystemCodes plugin is loaded."""
        ...
