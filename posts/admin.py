from django.conf import settings
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from ckeditor.widgets import CKEditorWidget

from models import Category, CategoryResource, Post, PostResource
from import_export.admin import ImportExportModelAdmin
import reversion


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    formats = settings.IMPORT_EXPORT_FORMATS

admin.site.register(Category, CategoryAdmin)


class PostAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = PostResource
    save_as = True
    formats = settings.IMPORT_EXPORT_FORMATS

    def url_link(self):
        return '<a href="/%s/%s">View</a>' % (settings.POSTS_URL_PREFIX, self.url.lstrip('/'))
    url_link.allow_tags = True

    def preview_url_link(self):
        return '<a href="/%s/%s">View</a>' % (settings.POSTS_URL_PREFIX, self.preview_url.lstrip('/'))
    preview_url_link.allow_tags = True


    list_display = ('created_at', 'publish_time', 'title', url_link , preview_url_link ,
                    'is_draft', 'exclude_from_sitemap', 'post_ranking', 'sitemap_priority', 'author', )
    list_filter = ('is_draft', 'exclude_from_sitemap', 'author')
    search_fields = ('url', 'preview_url', 'title')
    exclude = ('preview_url', 'preview_text')
    prepopulated_fields = {"url": ("title",)}

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }

admin.site.register(Post, PostAdmin)
