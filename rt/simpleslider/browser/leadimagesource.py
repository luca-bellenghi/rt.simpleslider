# -*- coding: utf-8 -*-

from zope.component import adapts, getMultiAdapter
from zope.interface import implements
from zope.publisher.interfaces.browser import IBrowserView
from Products.Archetypes.interfaces.base import IBaseObject
from collective.contentleadimage.interfaces import ILeadImageable,\
     ILeadImageSpecific
from collective.contentleadimage.config import IMAGE_FIELD_NAME
from collective.contentleadimage.config import IMAGE_CAPTION_FIELD_NAME

from rt.simpleslider.interfaces import ISliderSource


class ContentLeadImageSliderSource(object):

    implements(ISliderSource)
    adapts(IBrowserView, IBaseObject, ILeadImageSpecific)

    def __init__(self, view, context, request):
        self.context = context
        self.request = request
        self.view = view

    def items(self):
        if ILeadImageable.providedBy(self.context):
            return [self.context]
        return 

    def getCaption(self):
        if not ILeadImageable.providedBy(self.context):
            return self.context.title_or_id()

        field = self.context.getField(IMAGE_CAPTION_FIELD_NAME)
        caption = field.get_size(self.context) != 0
        if not caption:
            return self.context.title_or_id()
        else:
            return field.get(self.context)

    def getImage(self):
        if not ILeadImageable.providedBy(self.context):
            return ''
        else:
            caption = self.getCaption()
            field = self.context.getField(IMAGE_FIELD_NAME)
            return field.tag(self.context, title=caption)

    def getSliderImages(self):
        for item in self.items():
            slider = getMultiAdapter((self.view, item, self.request),
                                     ISliderSource)
            img = slider.getImage()
            yield img
