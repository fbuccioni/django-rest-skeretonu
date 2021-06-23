"""
Admin main file example with an automatic add of Admin classes passing the module
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as gettext

from . import skeretonu
from ..skeretonu import models


class AdminSite(admin.sites.AdminSite):
    # Text to put at the end of each page's <title>.
    sitegettextitle = gettext('Skeretonu admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = gettext('Skeretonu admin')

    # Text to put at the top of the admin index page.
    indexgettextitle = gettext('Administration')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)


site = AdminSite()

# If you don't want to admins manually, here is an example
#site.register(
#    skeretonu.models.Skeretonu, skeretonu.SkeretonuAdmin
#)

# Automatic import from modules with Admin classes
for admin_module in (skeretonu,):
    for item in dir(admin_module):
        if hasattr(item, 'ignore_auto'):
            continue

        model_admin = getattr(admin_module, item)
        try:
            is_class = issubclass(model_admin, object)
        except TypeError:
            is_class = False

        if is_class and issubclass(model_admin, admin.ModelAdmin):
            try:
                site.register(getattr(models, item), model_admin)
            except:
                pass
