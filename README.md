# django-pytz-timezone-field

This is a simple field which returns a timezone from the PYTZ package.

It presents itself as a Select widget (by default) that utilizes opt-groups.

The form-field portion of this package can happily work with existing CharFields, or just used the PYTZTimeZoneField in your model.

The `choices` are maintained in the form field, not in the model field. This allows PYTZ to be upgraded regularly without incurring schema migrations.