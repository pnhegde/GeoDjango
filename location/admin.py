from django.contrib import admin

from location.models import PolygonAddress

class PolygonAddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    ordering = ('-id',)


admin.site.register(PolygonAddress, PolygonAddressAdmin)
