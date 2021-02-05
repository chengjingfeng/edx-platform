# -*- coding: utf-8 -*-
"""
NexBlock-framework-as-an-XBlock prototype.
"""

import logging
from xblock.core import XBlock
from xblock.fields import Scope, String, UNIQUE_ID
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin


log = logging.getLogger(__name__)
loader = ResourceLoader(__name__)  # pylint: disable=invalid-name


def _(text):
    """
    A noop underscore function that marks strings for extraction.
    """
    return text


@XBlock.needs('user')  # pylint: disable=abstract-method
@XBlock.needs('i18n')
class NexXBlock(XBlock, StudioEditableXBlockMixin):  # lint-amnesty, pylint: disable=abstract-method
    """
    NexBlock!
    """

    editable_fields = []  # @@TODO

    has_author_view = True  # Tells Studio to use author_view

    @property
    def course_key(self):
        """
        :return: int course id

        NB: The goal is to move this XBlock out of edx-platform, and so we use
        scope_ids.usage_id instead of runtime.course_id so that the code will
        continue to work with workbench-based testing.
        """
        return getattr(self.scope_ids.usage_id, 'course_key', None)

    @property
    def django_user(self):
        """
        Returns django user associated with user currently interacting
        with the XBlock.
        """
        user_service = self.runtime.service(self, 'user')
        if not user_service:
            return None
        return user_service._django_user  # pylint: disable=protected-access

    @staticmethod
    def vendor_js_dependencies():
        """
        Returns list of vendor JS files that this XBlock depends on.

        The helper function that it uses to obtain the list of vendor JS files
        works in conjunction with the Django pipeline to ensure that in development mode
        the files are loaded individually, but in production just the single bundle is loaded.
        """
        return get_js_dependencies('discussion_vendor')

    @staticmethod
    def js_dependencies():
        """
        Returns list of JS files that this XBlock depends on.

        The helper function that it uses to obtain the list of JS files
        works in conjunction with the Django pipeline to ensure that in development mode
        the files are loaded individually, but in production just the single bundle is loaded.
        """
        return get_js_dependencies('discussion')

    @staticmethod
    def css_dependencies():
        """
        Returns list of CSS files that this XBlock depends on.

        The helper function that it uses to obtain the list of CSS files
        works in conjunction with the Django pipeline to ensure that in development mode
        the files are loaded individually, but in production just the single bundle is loaded.
        """
        raise NotImplementedError

    def add_resource_urls(self, fragment):
        """
        Adds URLs for JS and CSS resources that this XBlock depends on to `fragment`.
        """
        raise NotImplementedError

    def has_permission(self, permission):
        """
        Encapsulates lms specific functionality, as `has_permission` is not
        importable outside of lms context, namely in tests.

        :param user:
        :param str permission: Permission
        :rtype: bool
        """
        raise NotImplementedError

    def student_view(self, context=None):
        """
        Renders student view for LMS.
        """

        raise NotImplementedError

    def author_view(self, context=None):  # pylint: disable=unused-argument
        """
        Renders author view for Studio.
        """
        raise NotImplementedError

    def student_view_data(self):
        """
        Returns a JSON representation of the student_view of this XBlock.
        """
        raise NotImplementedError

    @classmethod
    def parse_xml(cls, node, runtime, keys, id_generator):
        """
        Parses OLX into XBlock.
        """
        raise NotImplementedError
