from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from django.conf import settings

from models import Section, SectionResource, Page, PageResource

from django_ace import AceWidget
from import_export.admin import ImportExportModelAdmin
import reversion


class SectionAdmin(ImportExportModelAdmin):
    resource_class = SectionResource
    formats = settings.IMPORT_EXPORT_FORMATS

admin.site.register(Section, SectionAdmin)


class PageAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = PageResource
    save_as = True
    formats = settings.IMPORT_EXPORT_FORMATS

    def url_link(self):
        return '<a href="/%s">View</a>' % self.url.lstrip('/')
    url_link.allow_tags = True

    def preview_url_link(self):
        return '<a href="/%s">View</a>' % self.preview_url.lstrip('/')
    preview_url_link.allow_tags = True


    list_display = ('section', url_link , preview_url_link ,'is_draft', 'exclude_from_sitemap')
    list_filter = ('is_draft', 'exclude_from_sitemap', 'section')
    search_fields = ('url', 'preview_url')
    exclude = ('preview_url',)

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': AceWidget(mode='html', width='750px', height='700px')},
    }

admin.site.register(Page, PageAdmin)
