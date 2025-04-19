from django.contrib import admin
from myapp.models import PemainBola, Klub

class PemainBolaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'id', 'domisili']

class KlubAdmin(admin.ModelAdmin):
    list_display = ['nama', 'negara']

admin.site.register(PemainBola, PemainBolaAdmin)
admin.site.register(Klub, KlubAdmin)
