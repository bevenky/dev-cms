"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'dev-cms.menu.CustomMenu'
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class CMSMenu(Menu):
    """
    CMS Menu for dev-cms admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.AppList(
                _('Content'),
                models=('posts.*', 'pages.*', 'appearance.*', 'fack.*')
            ),
            items.AppList(
                _('Administration'),
                models=('django.contrib.*',)
            ),
            items.AppList(
                _('Tools'),
                models=('redirects.*', 'reversion.*')
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CMSMenu, self).init_with_context(context)
