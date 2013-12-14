import random, string

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Theme(models.Model):
    ''' Theme in which templates reside for logical filtering in the admin
    '''
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = _('theme')
        verbose_name_plural = _('themes')

    def __unicode__(self):
        return self.name


class Template(models.Model):
    '''A DB backed Django Template
    '''
    theme = models.ForeignKey(Theme)
    path = models.CharField(max_length=500, db_index=True,
        help_text="Logical path, not a URL e.g. 'theme/folder/template.html'")
    description = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(_('creation at'),
                                         auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'),
                                        auto_now=True)

    class Meta:
        verbose_name = _('template')
        verbose_name_plural = _('templates')
        ordering = ('theme',)

    def __unicode__(self):
        return u'%s - %s'  % (self.theme, self.path)

