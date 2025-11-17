"""
WSGI config for devgege_project.
"""

import os

# Importação correta:
from django.core.wsgi import get_wsgi_application

# Aponta para o arquivo de settings que acabamos de configurar
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
