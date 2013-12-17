from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from models import Category, Page

from django_ace import AceWidget
import reversion


admin.site.register(Category)


class PageAdmin(reversion.VersionAdmin):

    def url_link(self):
        return '<a href="/%s">%s</a>' % (self.url.lstrip('/'), self.url)
    url_link.allow_tags = True

    def preview_url_link(self):
        return '<a href="/%s">%s</a>' % (self.preview_url.lstrip('/'), self.preview_url)
    preview_url_link.allow_tags = True


    list_display = ('category', url_link , preview_url_link ,'is_draft', 'exclude_from_sitemap')
    list_filter = ('is_draft', 'exclude_from_sitemap', 'category')
    search_fields = ('url', 'preview_url')
    exclude = ('preview_url',)

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': AceWidget(mode='html', width='1350px', height='450px')},
    }
admin.site.register(Page, PageAdmin)
