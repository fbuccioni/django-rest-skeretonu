"""
django-skeretonu.rst admin file example.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _t

from . import skeretonu
from ..skeretonu import models


class AdminSite(admin.sites.AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = _t('Skeretonu admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = _t('Skeretonu admin')

    # Text to put at the top of the admin index page.
    index_title = _t('Administration')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)


site = AdminSite()

#site.register(
#    skeretonu.models.Skeretonu, skeretonu.SkeretonuAdmin
#)


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