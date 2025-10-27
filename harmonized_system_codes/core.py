"""Support harmonized system codes against sales orders"""

from plugin import InvenTreePlugin

from plugin.mixins import (
    AppMixin,
    EventMixin,
    ReportMixin,
    SettingsMixin,
    UrlsMixin,
    UserInterfaceMixin,
)

from . import PLUGIN_VERSION


class HarmonizedSystemCodes(
    AppMixin,
    EventMixin,
    ReportMixin,
    SettingsMixin,
    UrlsMixin,
    UserInterfaceMixin,
    InvenTreePlugin,
):
    """HarmonizedSystemCodes - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "Harmonized System Codes"
    NAME = "HarmonizedSystemCodes"
    SLUG = "harmonized-system-codes"
    DESCRIPTION = "Support harmonized system codes against sales orders"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "Oliver Walters"
    WEBSITE = "https://github.com/SchrodingersGat/inventree-harmoized-codes"
    LICENSE = "MIT"

    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'

    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        "CUSTOM_VALUE": {
            "name": "Custom Value",
            "description": "A custom value",
            "validator": int,
            "default": 42,
        }
    }

    # Respond to InvenTree events (from EventMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/event/
    def wants_process_event(self, event: str) -> bool:
        """Return True if the plugin wants to process the given event."""
        # Example: only process the 'create part' event
        return event == "part_part.created"

    def process_event(self, event: str, *args, **kwargs) -> None:
        """Process the provided event."""
        print("Processing custom event:", event)
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

    # Custom report context (from ReportMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/report/
    def add_label_context(
        self, label_instance, model_instance, request, context, **kwargs
    ):
        """Add custom context data to a label rendering context."""

        # Add custom context data to the label rendering context
        context["foo"] = "label_bar"

    def add_report_context(
        self, report_instance, model_instance, request, context, **kwargs
    ):
        """Add custom context data to a report rendering context."""

        # Add custom context data to the report rendering context
        context["foo"] = "report_bar"

    def report_callback(self, template, instance, report, request, **kwargs):
        """Callback function called after a report is generated."""
        ...

    # Custom URL endpoints (from UrlsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/urls/
    def setup_urls(self):
        """Configure custom URL endpoints for this plugin."""
        from django.urls import path
        from .views import HarmonizedSystemCodeList, HarmonizedSystemCodeDetail

        return [
            # Provide path to a simple custom view - replace this with your own views
            path(
                "<int:pk>/",
                HarmonizedSystemCodeDetail.as_view(),
                name="harmonizedsystemcode-detail",
            ),
            path(
                "", HarmonizedSystemCodeList.as_view(), name="harmonizedsystemcode-list"
            ),
        ]

    # User interface elements (from UserInterfaceMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/ui/

    def display_codes_panel(self, request, context: dict, **kwargs):
        """Determine whether to display the harmonized system codes panel."""

        from company.models import Company

        target_model = context.get("target_model", None)
        target_id = context.get("target_id", None)

        # Always display on the admin center
        if target_model == "admincenter":
            return True

        # Display for customers
        if target_model == "company" and target_id:
            try:
                company = Company.objects.filter(pk=target_id).first()
                if company and company.is_customer:
                    return True
            except (Company.DoesNotExist, ValueError):
                return False

        # Default: do not display
        return False

    # Custom UI panels
    def get_ui_panels(self, request, context: dict, **kwargs):
        """Return a list of custom panels to be rendered in the InvenTree user interface."""

        panels = []

        # TODO: Look at the group that the user is in

        if self.display_codes_panel(request, context, **kwargs):
            panels.append({
                "key": "harmonized-system-codes-panel",
                "title": "Harmonized Codes",
                "description": "Display harmonized system codes",
                "icon": "ti:flag-search:outline",
                "source": self.plugin_static_file(
                    "Panel.js:renderHarmonizedSystemCodesPanel"
                ),
                "context": {
                    # Provide additional context data to the panel
                    "settings": self.get_settings_dict(),
                },
            })

        return panels
