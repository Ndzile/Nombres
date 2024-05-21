from django.contrib import admin

from nombres.models import CoordinationLocale, MembreBureauRegional, Region, Jeune

admin.site.register(CoordinationLocale)
admin.site.register(MembreBureauRegional)
admin.site.register(Region)
admin.site.register(Jeune)
