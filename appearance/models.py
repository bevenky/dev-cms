import random, string

from django.db import models
from django.utils.translation import ugettext_lazy as _

from import_export import resources


class Theme(models.Model):
    ''' Theme in which templates reside for logical filtering in the admin
    '''
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = _('theme')
        verbose_name_plural = _('themes')

    def __unicode__(self):
        return self.name


class ThemeResource(resources.ModelResource):

    class Meta:
        model = Theme


class Template(models.Model):
    '''A DB backed Django Template
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    theme = models.ForeignKey(Theme)
    path = models.CharField(max_length=500, db_index=True,
        help_text="Logical path, not a URL e.g. 'theme/folder/template.html'")
    description = models.CharField(max_length=200, blank=True)
    content = models.TextField()


    class Meta:
        verbose_name = _('template')
        verbose_name_plural = _('templates')
        ordering = ('theme',)

    def __unicode__(self):
        return u'%s - %s'  % (self.theme, self.path)


class TemplateResource(resources.ModelResource):

    class Meta:
        model = Template
