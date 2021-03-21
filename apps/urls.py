"""
URL Configuration for proeject
"""

from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

import apps.skeretonu.urls

urlpatterns = [
    path('_/jet/', include('jet.urls', 'jet')),
    path('js/i18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    path('', include(apps.skeretonu.urls))
]
