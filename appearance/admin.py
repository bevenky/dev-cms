from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from models import Template, Theme

from django_ace import AceWidget
import reversion


admin.site.register(Theme)


class TemplateAdmin(reversion.VersionAdmin):
    save_as = True

    list_display = ( 'path', 'theme', 'description' ,'created_at', 'updated_at')
    search_fields = ('path', 'description')
    list_filter = ('theme',)

    formfield_overrides = {
        models.TextField: {'widget': AceWidget(mode='html', width='1200px', height='450px')},

    }
admin.site.register(Template, TemplateAdmin)
