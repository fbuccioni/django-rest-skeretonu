"""
URL Configuration for proeject
"""

from django.contrib import admin
from django.urls import path, include
import apps.skeretonu.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(apps.skeretonu.urls))
]
