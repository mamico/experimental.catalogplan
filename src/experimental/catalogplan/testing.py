# -*- coding: utf-8 -*-
from plone.app.testing.layers import FunctionalTesting
from Products.CMFPlone.testing import ProductsCMFPloneLayer


class BaseLayer(ProductsCMFPloneLayer):
    def setUpZope(self, app, configurationContext):  # pylint: disable=W0613
        # import experimental.catalogplan
        pass


BASE = BaseLayer()


BASE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BASE, ),
    name="experimental.noacquisiton:Functional"
)
