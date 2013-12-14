# Template loader to retrieve templates from the database
from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader

from pages.models import Page
from appearance.models import Template


class DBTemplateLoader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        try:
            if template_name.startswith('/preview/'):
                page = Page.objects.get(preview_url__exact=template_name)
            else:
                page = Page.objects.get(url__exact=template_name)
            return page.content, str(page)
        except Page.DoesNotExist:
            try:
                tmpl = Template.objects.get(path__exact=template_name)
                return tmpl.content, str(tmpl)
            except Template.DoesNotExist:
                raise TemplateDoesNotExist, template_name
