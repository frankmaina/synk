# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()