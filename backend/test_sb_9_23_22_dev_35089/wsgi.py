"""
WSGI config for test_sb_9_23_22_dev_35089 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_sb_9_23_22_dev_35089.settings')

application = get_wsgi_application()
