"""
Tests for the rss_proxy models
"""


import six
from django.test import TestCase

from lms.djangoapps.rss_proxy.models import WhitelistedRssUrl


class WhitelistedRssUrlTests(TestCase):
    """ Tests for the rss_proxy.WhitelistedRssUrl model """

    def setUp(self):
        super(WhitelistedRssUrlTests, self).setUp()  # lint-amnesty, pylint: disable=super-with-arguments
        self.whitelisted_rss_url = WhitelistedRssUrl.objects.create(url='http://www.example.com')

    def test_unicode(self):
        """
        Test the unicode function returns the url
        """
        self.assertEqual(six.text_type(self.whitelisted_rss_url), self.whitelisted_rss_url.url)
