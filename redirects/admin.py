from django.contrib import admin
from django.conf import settings

from models import Redirect, RedirectResource

from import_export.admin import ImportExportModelAdmin


class RedirectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RedirectResource
    formats = settings.IMPORT_EXPORT_FORMATS

    list_display = ('old_url', 'new_url')
    search_fields = ('old_url', 'new_url')

admin.site.register(Redirect, RedirectAdmin)
