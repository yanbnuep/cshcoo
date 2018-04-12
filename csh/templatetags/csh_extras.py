from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.filter(name='times')
def times(number):
    return range(number)


@register.filter(name='js')
def js(obj):
    return mark_safe(json.dumps(obj, indent=4, sort_keys=True, default=str))


@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a, b)
