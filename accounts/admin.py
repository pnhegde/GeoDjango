from django.contrib import admin

from accounts.models import TransportOperator


class TransportOperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')


admin.site.register(TransportOperator, TransportOperatorAdmin)
