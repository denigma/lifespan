from selectable.base import LookupBase, ModelLookup
from selectable.registry import registry
from models import Member,Organization
from selectable.forms import base
import selectable
from selectable.forms import widgets,fields
from django import forms
import django


class OrganizationLookup(ModelLookup):
    model = Organization
    search_fields = ('name__icontains', )

    def get_item_value(self, item):
        # Display for currently selected item
        return item.name

    def get_item_label(self, item):
        # Display for choice listings
        return item.name

registry.register(OrganizationLookup)



class OrganizationForm(forms.Form):
    city = fields.AutoCompleteSelectField(
        lookup_class=OrganizationLookup,
        label='Organization',
        required=False,
        widget=widgets.AutoComboboxSelectWidget
    )
