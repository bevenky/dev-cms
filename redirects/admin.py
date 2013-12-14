from django.contrib import admin
from models import Redirect


class RedirectAdmin(admin.ModelAdmin):
    list_display = ('old_url', 'new_url')
    search_fields = ('old_url', 'new_url')

admin.site.register(Redirect, RedirectAdmin)
