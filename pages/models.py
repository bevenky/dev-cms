import random, string

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Section(models.Model):
    ''' Section in which pages reside for logical filtering in the admin
    '''
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')

    def __unicode__(self):
        return self.name


class Page(models.Model):
    ''' Actual Pages which use templates and provide content for the blocks
        and map to a URL
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    url = models.CharField(max_length=512, unique=True, db_index=True,
            help_text = "This should be an absolute url, excluding the domain name. e.g. '/urlpath/actualurl/'")
    preview_url = models.CharField(max_length=512, unique=True)
    section = models.ForeignKey(Section, blank=True, null=True,)
    is_draft = models.BooleanField(default=False, help_text='If True, page will not be made public')
    exclude_from_sitemap = models.BooleanField(default=False, help_text='If True, page will be exlcuded from sitemap')
    sitemap_priority = models.DecimalField(default='0.5', decimal_places=1, max_digits=2)
    content = models.TextField(blank=True)


    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        ordering = ('section',)

    def __unicode__(self):
        return u'%s' % (self.url)

    def gen_preview_prefix(self):
        return ''.join(random.sample(string.lowercase+string.digits,10))

    def save(self, *args, **kwargs):
        self.url = self.url.strip('/')
        self.url = "/%s/" % self.url
        self.preview_url = "/preview/%s%s" % (self.gen_preview_prefix(), self.url)
        super(Page, self).save(*args, **kwargs)





