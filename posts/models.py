import random, string
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from filer.fields.image import FilerImageField


class Category(models.Model):
    ''' Category in which posts reside for logical filtering in the admin
    '''
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__(self):
        return self.name


class Post(models.Model):
    ''' Actual Post which is used to write content
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=512, help_text = "Title of the post")
    url = models.CharField(max_length=512, unique=True, db_index=True,
            help_text = "This should be an absolute url, excluding the prefix of the domain. e.g. '/urlpath/actualurl/'")
    author = models.ForeignKey(User, help_text = "Title of the post")

    preview_url = models.CharField(max_length=512, unique=True)
    category = models.ManyToManyField(Category, blank=True, null=True,)
    is_draft = models.BooleanField(default=False,
                help_text='If True, page will not be made public')
    meta_description = models.CharField(max_length=180,
                help_text = "Meta Description for the post")
    meta_keywords = models.CharField(max_length=180,
                help_text = "Meta Keywords for the post")
    preview_image = FilerImageField(null=True, blank=True)
    preview_text = models.TextField(blank=True,
                help_text = "Preview text which shows up in the listing of posts")
    publish_time = models.DateTimeField(default=datetime.now,
            help_text='schedule posting go live')
    exclude_from_sitemap = models.BooleanField(default=False,
            help_text='If True, page will be exlcuded from sitemap')
    sitemap_priority = models.DecimalField(default='0.5', decimal_places=1, max_digits=2)
    post_ranking = models.IntegerField(default=1,
            help_text="ranking based on which the post will show up in top posts list")
    related_posts = models.ManyToManyField('self', blank=True, null=True,)
    content = models.TextField(blank=True,
                help_text="Actual content goes here. Preview text -{# previewend #}")


    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('created_at',)

    def __unicode__(self):
        return u'%s' % (self.url)

    def gen_preview_prefix(self):
        return ''.join(random.sample(string.lowercase+string.digits,10))

    def save(self, *args, **kwargs):
        self.url = self.url.strip('/')
        self.url = "/%s/" % self.url
        self.preview_url = "/preview/%s%s" % (self.gen_preview_prefix(), self.url)
        self.preview_text = self.content.split("{# previewend #}")[0][:499]
        super(Post, self).save(*args, **kwargs)

