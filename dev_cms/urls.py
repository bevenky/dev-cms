from django.conf.urls import patterns, include, url
from django.conf import settings
from django.http import HttpResponse

from pages.views import render_page, render_preview_page
from pages.sitemap import PagesSitemap

from django.contrib import admin
admin.autodiscover()


# info_dict = {
#     'queryset': Posts.objects.all(),
#     'date_field': 'created_at',
# }


sitemaps = {
    'static': PagesSitemap,
    # 'blog': GenericSitemap(info_dict, priority=0.6),
}

# Return a robots.txt that disallows all spiders when DEBUG is True and vice versa
if getattr(settings, "DEBUG", False):
    urlpatterns = patterns("",
        ("^robots.txt$", lambda r: HttpResponse("User-agent: *\nDisallow: /",
                                                mimetype="text/plain")),
    )
else:
    urlpatterns = patterns("",
        ("^robots.txt$", lambda r: HttpResponse("User-agent: *\nDisallow: ",
                                                mimetype="text/plain")),
    )


urlpatterns += patterns('',
    # Admin-tools URL
    url(r'^admin_tools/', include('admin_tools.urls')),

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Sitemap URL
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # FAQ URL
    url(r'^faq/', include('fack.urls')),

    # WYSIWYG
    url(r'^ckeditor/upload/', 'ckeditor.views.upload', name='ckeditor_upload'),
    url(r'^ckeditor/browse/', 'ckeditor.views.browse', name='ckeditor_browse'),

     # All Preview URLs here
    url(r'^%s/' %settings.POSTS_PREFIX, include('posts.urls')),

     # All Preview URLs here
    url(r'^preview/(?P<path>.*)$', render_preview_page),

    # All Dynamic URLs caught here
    (r'^(?P<path>.*)$', render_page),

)

