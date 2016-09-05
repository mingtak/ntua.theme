# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ntua.theme.testing import NTUA_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that ntua.theme is properly installed."""

    layer = NTUA_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ntua.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ntua.theme'))

    def test_browserlayer(self):
        """Test that INtuaThemeLayer is registered."""
        from ntua.theme.interfaces import (
            INtuaThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(INtuaThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NTUA_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ntua.theme'])

    def test_product_uninstalled(self):
        """Test if ntua.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ntua.theme'))

    def test_browserlayer_removed(self):
        """Test that INtuaThemeLayer is removed."""
        from ntua.theme.interfaces import INtuaThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(INtuaThemeLayer, utils.registered_layers())
