from django.contrib.sitemaps import Sitemap
from models import Page


class PagesSitemap(Sitemap):
    changefreq = "weekly"

    def priority(self, obj):
        return obj.sitemap_priority

    def items(self):
        return Page.objects.filter(exclude_from_sitemap=False, is_draft=False)

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return "/%s" % obj.url
