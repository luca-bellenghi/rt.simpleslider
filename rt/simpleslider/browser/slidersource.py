# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements
from zope.publisher.interfaces.browser import IBrowserView
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from Products.Archetypes.interfaces.base import IBaseObject

from rt.simpleslider.interfaces import ISliderSource


class GenericSliderSource(object):

    implements(ISliderSource)
    adapts(IBrowserView, IBaseObject, IDefaultBrowserLayer)

    def __init__(self, view, context, request):
        self.context = context
        self.request = request
        self.view = view

    def getSliderImages(self):
        return list(self.map_source.getSliderImages())[:6]

    def getSliderCaption(self):
        return list(self.map_source.getSliderCaption())[:6]
