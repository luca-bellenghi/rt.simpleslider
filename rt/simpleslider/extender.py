# -*- coding: utf-8 -*-
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget
from zope.component import adapts
from zope.interface import implements
from zope.component._api import getUtilitiesFor, getUtility

from Products.Archetypes.interfaces.base import IBaseObject
from Products.Archetypes.Field import StringField, TextField, ReferenceField
from Products.Archetypes.Widget import SelectionWidget, RichWidget
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot

from rt.simpleslider.browser.controlpanel import IControlPanel
from rt.simpleslider import MessageFactory as _


class TextField(ExtensionField, TextField):
    """ A trivial text area field """


class StringField(ExtensionField, StringField):
    """ A trivial string field """


class ReferenceField(ExtensionField, ReferenceField):
    """ A trivial ReferenceField field """


class BaseSchemaExtender(object):
    adapts(IBaseObject)
    implements(ISchemaExtender)

    def __init__(self, context):
        self.context = context
    fields = []

    def getFields(self):
        if not len(tuple(getUtilitiesFor(IPloneSiteRoot))):
            return []
        portal = getUtility(IPloneSiteRoot)
        pprop = IControlPanel(portal)
        if pprop is not None:
            portal_type = getattr(self.context, 'portal_type', None)
            if portal_type in getattr(pprop, self._attr):
                return self.fields
        return []


class SchemaExtender(BaseSchemaExtender):
    _attr = 'simpleslider_allowed_types'

    fields = [
        StringField('show_slider',
           schemata='settings',
           default = 'parent',
           vocabulary_factory='simpleslider.displayvocabulary',
           widget=SelectionWidget(
              label=_(u'Show slider in header'),
              description=_(u'If selected will display slider in top viewlet (only if slider source is found).\
                              You can decide to use parent configuration or override manualy here.'),
              ),
        ),
        ReferenceField('slider_source',
            relationship='slider_source',
            schemata='settings',
            multiValued=False,
            widget=ReferenceBrowserWidget(
                label=_(u'Slider source'),
                description=_(u'Relation with other objects to show slider.'),
                force_close_on_insert=True,
                ),
            ),
        TextField('slider_description',
         schemata='settings',
         default_content_type = 'text/html',
         default_output_type = 'text/x-html-safe',
         widget=RichWidget(
            label=_(u'Slider description'),
            description=_(u"Write here some description that will compare in the slider. Please, use subtitles ('h3' tag) to correctly show title in the slider")
            ),
         ),
    ]
