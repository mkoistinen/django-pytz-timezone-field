# -*- coding: utf-8 -*-
import pytz

from django import forms
from django.utils.translation import gettext_lazy as _

from ..utils import cached_property


class TimeZoneInputField(forms.ChoiceField):
    """
    This is a timezone field that computes the available timezone options from
    the current version of pytz and humanizes it a bit for rendering in the
    normal Select widget using opt-groups.
    """
    widget = forms.Select
    excluded_regions = ('Arctic', 'Antarctica')
    regionless_first = False
    regionless_label = _('Special')

    def __init__(self, **kwargs):
        """
        Constructor for the TimeZoneField. These options are supported:
        `excluded_regions`, any regions provided in an iterable here will be
            excluded from display. Default: ('Arctic', 'Antarctica')
        `regionless_first`, if set, the regionless items will be grouped at the
            top of the list, otherwise the bottom of the list. Default: False
        `regionless_label`, if set, determines the group name of the regionless
            items. Default: _('Special')
        :param kwargs:
        """
        if 'excluded_regions' in kwargs:
            self.excluded_regions = kwargs.pop('excluded_regions')
        if 'regionless_first' in kwargs:
            self.regionless_first = kwargs.pop('regionless_first')
        if 'regionless_label' in kwargs:
            self.regionless_label = kwargs.pop('regionless_label')
        if 'choices' not in kwargs:
            kwargs['choices'] = self.time_zone_choices
        super().__init__(**kwargs)

    @cached_property
    def time_zone_choices(self):
        """
        Returns a reasonably humanized set of timezone choices from the current
        version of pytz. This only needs to happen at startup, since the pytz
        version won't change after that, so we cache the result.

        :return: choices list
        """
        tz_list = []
        regionless = []
        current_region = ''
        region_list = []

        for tz in pytz.common_timezones:
            try:
                region, zone = tz.split('/', 1)

                if region in self.excluded_regions:
                    continue

                if region != current_region:
                    if region_list:
                        tz_list.append((current_region, region_list))
                        region_list = []
                    current_region = region

                region_list.append((tz, zone.replace('_', ' ')))

            except ValueError:
                # This didn't have a region, just collect these for now.
                if region_list:
                    tz_list.append((current_region, region_list))
                    region_list = []
                current_region = ''
                regionless.append((tz, tz))

        if region_list:
            tz_list.append((current_region, region_list))

        # Re-combine the lists
        if self.regionless_first:
            tz_list = [(self.regionless_label, regionless)] + tz_list
        else:
            tz_list += [(self.regionless_label, regionless)]

        return tz_list
