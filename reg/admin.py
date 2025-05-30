from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Per,Gab,Opt,Op

admin.site.register(Opt)
admin.site.register(Op)

class PerAdmin(admin.ModelAdmin):
    search_fields = ['cir' ]
    pass
admin.site.register(Per,PerAdmin)
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('cir', 'grup', 'pos', 'cd')

admin.site.register(Gab, BookAdmin)
