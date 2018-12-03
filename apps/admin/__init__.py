"""
django-skeretonu.rst admin file example.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# from . import skeretonu


class AdminSite(admin.sites.AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = _('Skeretonu admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = _('Skeretonu admin')

    # Text to put at the top of the admin index page.
    index_title = _('Administration')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)


site = AdminSite()

#site.register(
#    skeretonu.models.Skeretonu, skeretonu.SkeretonuAdmin
#)
