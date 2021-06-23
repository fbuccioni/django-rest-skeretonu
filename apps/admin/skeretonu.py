"""
App admin example, this file must have the name of the app

Don't add classes manually the classes automatically are added when have
the same name of the model, if you don't want to add it automatically
added use `ignore_auto` property as `True`
"""
from django.contrib import admin
from django.utils.safestring import mark_safe
#from ..skeretonu import models # Models from the app


# class SkeretonuAdmin(admin.ModelAdmin):
#     class Media:
#         model = models.Skeretonu
