[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/inventree-harmonized-system-codes)](https://pypi.org/project/inventree-harmonized-system-codes/)
![PEP](https://github.com/SchrodingersGat/inventree-harmonized-codes/actions/workflows/ci.yaml/badge.svg)

# Harmonized System Codes

An [InvenTree](https://inventree.org) plugin to support [harmonized system codes](https://en.wikipedia.org/wiki/Harmonized_System) (HS codes) against sales orders and shipments.

## Installation

### InvenTree Plugin Manager

The recommended method to install this plugin is via the InvenTree Plugin Manager.

### Command Line 

To install manually via the command line, run the following command:

```bash
pip install inventree-harmonized-system-codes
```

## Setup

### Activate the Plugin

... todo ...

### Run Migrations

... todo ...

## Configuration

... todo ...

## Usage

### Specifying Harmonized System Codes

To specify Harmonized System Codes (HS codes) for parts, navigate to the "Harmonized System Codes" section in the InvenTree admin interface. Here, you can create new HS codes and associate them with specific part categories. You can also specify customer-specific HS codes if needed.

When creating or editing a part, ensure that the part is assigned to a category that has an associated HS code.

### Customer Specific Codes

If desired, you can create customer-specific HS codes by selecting a customer when creating the HS code entry. This allows you to override the generic HS code for specific customers.

### Report Template Tags

The plugin provides a custom template tag to extract the Harmonized System Code associated with any part in a report.

To use the template tag, first load the `harmonized_codes` template library at the top of your report template:

```django
{% load harmonized_codes %}
```

Then, you can use the `harmonized_code` tag to retrieve the HS code for a given part. Note that the customer should also be supplied, in case there is a customer-specific HS code associated with the part.

For example, in the context of a SalesOrderShipment report:

```django

{% for allocation in allocations.all %}
    {% harmonized_code allocation.line.part customer=order.customer as hs_code %}
    <tr>
        <td>{{ allocation.line.part.full_name }}</td>
        <td>{% if hs_code %}{{ hs_code.code }}{% else %}N/A{% endif %}</td>
    </tr>
{% endfor %}
```
