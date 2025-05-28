# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def format_price(value):
    """Format price in Kenyan Shillings"""
    try:
        value = float(value)
        return mark_safe(f'KES {value:,.2f}')
    except (ValueError, TypeError):
        return value 