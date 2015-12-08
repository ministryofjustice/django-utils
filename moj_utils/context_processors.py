from django.conf import settings


def debug(request):
    return {'DEBUG': settings.DEBUG}


def analytics(request):
    return {'GOOGLE_ANALYTICS_ID': getattr(settings, 'GOOGLE_ANALYTICS_ID')}
