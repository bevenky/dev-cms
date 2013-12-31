from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from import_export import resources


class Redirect(models.Model):
    old_url = models.CharField(_('redirect from'), unique=True, max_length=512, db_index=True,
        help_text=_("This should be an absolute url, excluding the domain name. Example: '/events/search/'."))
    new_url = models.CharField(_('redirect to'), max_length=512, blank=True,
        help_text=_("This should an absolute url (as above)"))

    class Meta:
        verbose_name = _('redirect')
        verbose_name_plural = _('redirects')
        ordering = ('old_url',)

    def __str__(self):
        return "%s ---> %s" % (self.old_url, self.new_url)



class RedirectResource(resources.ModelResource):

    class Meta:
        model = Redirect
