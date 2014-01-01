from django.conf.urls import patterns, include, url
from django.conf import settings
from django.http import HttpResponse

from views import render_post, render_preview_post, render_post_listing, render_category_listing


urlpatterns = patterns('',
    # Blog Listing URL
    url(r'^$', render_post_listing),

    # Category Listing URL
    url(r'^category/(?P<category>.*)$', render_category_listing),

    # Author Listing URL
    url(r'^author/(?P<author>.*)$', render_author_listing),

    # All Preview URLs here
    url(r'^preview/(?P<path>.*)$', render_preview_post),

    # All Dynamic URLs caught here
    (r'^(?P<path>.*)$', render_post),

)

