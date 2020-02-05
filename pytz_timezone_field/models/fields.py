# -*- coding: utf-8 -*-
from django.db.models.fields import CharField

from ..forms.fields import TimeZoneInputField


class TimeZoneField(CharField):
    """
    A relatively dynamic TimeZone field for Django models.
    """
    def __init__(self, *args, **kwargs):
        # Note, as of this writing, the max length of the pytz timezone choices
        # is 30 characters.
        kwargs.setdefault('max_length', 63)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        # Use the companion TimeZoneInputField by default, note, the super()
        # call is quite intentionally bypassing our parent class.
        return super(CharField, self).formfield(**{
            'form_class': TimeZoneInputField,
            **kwargs,
        })
