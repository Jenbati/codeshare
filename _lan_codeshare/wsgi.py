import os

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    os.getenv('DJANGO_SETTINGS_MODULE', '_lan_codeshare.settings.production')
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
