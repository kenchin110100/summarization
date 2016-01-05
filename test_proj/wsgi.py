"""
WSGI config for test_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
#import sys

#sys.path.append('/var/www/cgi-bin/test_proj')
#sys.path.append('/var/www/cgi-bin/test_proj/test_proj')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_proj.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
