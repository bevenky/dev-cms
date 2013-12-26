from django.conf import settings
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from models import Category, Post

import reversion


admin.site.register(Category)


class PostAdmin(reversion.VersionAdmin):
    save_as = True

    def url_link(self):
        return '<a href="/%s/%s">%s</a>' % (settings.POSTS_PREFIX, self.url.lstrip('/'), self.url)
    url_link.allow_tags = True

    def preview_url_link(self):
        return '<a href="/%s/%s">%s</a>' % (settings.POSTS_PREFIX, self.preview_url.lstrip('/'), self.preview_url)
    preview_url_link.allow_tags = True


    list_display = ('created_at', 'publish_time', 'title', url_link , preview_url_link ,
                    'is_draft', 'exclude_from_sitemap', 'post_ranking', 'author')
    list_filter = ('is_draft', 'exclude_from_sitemap', 'author')
    search_fields = ('url', 'preview_url', 'title')
    exclude = ('preview_url', 'preview_text')
    prepopulated_fields = {"url": ("title",)}

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    }

admin.site.register(Post, PostAdmin)
