from django.shortcuts import render, get_object_or_404

from models import Page


def render_page(request, path):
    if path == "":
        page_url = "/"
    else:
        page_url =  path.strip('/')
        page_url = "/%s/" % page_url
    if request.user.is_authenticated():
        page = get_object_or_404(Page, url=page_url)
    else:
        page = get_object_or_404(Page, url=page_url, is_draft=False)
    return render(request, page_url)


def render_preview_page(request, path):
    page_url = "/preview/%s" % path
    page = get_object_or_404(Page, preview_url=page_url)
    return render(request, page_url)


