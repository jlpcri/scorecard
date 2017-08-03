from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter
def prepend_dollars(dollars):
    if dollars:
        return '$%s%s' % (intcomma(int(dollars)), ('%0.2f' % dollars)[-3:])
    else:
        return '$0.00'


@register.filter
def percentage_format(value):
    return '{0:.2f}%'.format(value * 100)


@register.filter
def percentage_result(value):
    return '{0:.2f}%'.format(value)

