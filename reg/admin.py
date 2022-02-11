from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Per,Gab,Opt

admin.site.register(Opt)
admin.site.register(Per)
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('cir', 'grup', 'pos', 'cd')

admin.site.register(Gab, BookAdmin)
