"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'dev-cms.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dev-cms.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class CMSIndexDashboard(Dashboard):
    """
    CMS index dashboard for dev-cms.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Content'),
             models=('posts.*', 'pages.*', 'appearance.*', 'redirects.*',
                    'fack.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            _('Administration'),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 14))


        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Navigation'),
            children=[
                {
                    'title': _('Homepage'),
                    'url': 'http://plivo.com/',
                    'external': True,
                },
                {
                    'title': _('Pricing'),
                    'url': 'http://plivo.com/pricing/',
                    'external': True,
                },
                {
                    'title': _('Docs'),
                    'url': 'http://plivo.com/docs/',
                    'external': True,
                },
                {
                    'title': _('Blog'),
                    'url': 'http://plivo.com/blog/',
                    'external': True,
                },
            ]
        ))


class CMSAppIndexDashboard(AppIndexDashboard):
    """
    CMS app index dashboard for dev-cms.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CMSAppIndexDashboard, self).init_with_context(context)
