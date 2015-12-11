from django import template

register = template.Library()


@register.filter()
def to_string(value):
    return str(value)


@register.filter(is_safe=True)
def safewrap(val, arg):
    return val.format(arg)


@register.filter()
def field_from_name(form, name):
    if name in form.fields:
        return form[name]


@register.inclusion_tag('moj_utils/sentry-js.html')
def sentry_js():
    try:
        from raven.contrib.django.models import client
    except ImportError:
        return None

    sentry_dsn = client.get_public_dsn('https') or None
    return {
        'sentry_dsn': sentry_dsn
    }
