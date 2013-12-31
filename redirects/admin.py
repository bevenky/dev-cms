from django.contrib import admin
from models import Redirect, RedirectResource

from import_export.admin import ImportExportModelAdmin


class RedirectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RedirectResource

    list_display = ('old_url', 'new_url')
    search_fields = ('old_url', 'new_url')

admin.site.register(Redirect, RedirectAdmin)
