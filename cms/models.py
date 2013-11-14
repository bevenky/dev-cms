from django.db import models

from django.template import Template as DjangoTemplate
from django.utils.translation import ugettext_lazy as _


class Template(models.Model):
    '''A DB backed Django Template'''
    path = models.CharField(max_length=500, db_index=True,
        help_text='This is NOT a URL')
    description = models.CharField(max_length=200, blank=True)
    content = models.TextField()

    class Meta:
        verbose_name = _('template')
        verbose_name_plural = _('templates')
        ordering = ('path',)

    def __unicode__(self):
        return self.path

    def render(self, context):
        return DjangoTemplate(self.content).render(context)
