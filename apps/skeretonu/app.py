import logging
import sys

from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig
from django.core.management import call_command

logging.addLevelName(logging.INFO,  'info ')
logging.addLevelName(logging.WARN,  'warn ')
logging.addLevelName(logging.ERROR, 'error')
logging.addLevelName(logging.DEBUG, 'debug')


class Config(AppConfig):
    name: str = "apps.skeretonu"
    label: str = "skeretonu"
    verbose_name: str = _("Skeretonu")

    # Auto migrate in production
    @classmethod
    def ready(cls):
        if (
            not sys.argv
            or not sys.argv[0].endswith("manage.py")
        ):
            call_command('migrate')
