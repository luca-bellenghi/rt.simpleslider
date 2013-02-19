# -*- coding: utf-8 -*-

from zope.interface import Interface, implements
from zope.formlib import form
from zope.event import notify
from zope import schema
from zope.component._declaration import adapts
from zope.component._api import getUtility, getMultiAdapter
from plone.app.controlpanel.form import ControlPanelForm
from plone.protect import CheckAuthenticator
from plone.app.controlpanel.events import ConfigurationChangedEvent

from Products.CMFPlone import PloneMessageFactory as _p
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.statusmessages.interfaces import IStatusMessage

from rt.simpleslider import MessageFactory as _


class IControlPanel(Interface):

        simpleslider_allowed_types = schema.Tuple(
                          title=_(u"Portal types for 'simpleslider' field"),
                          description=_(u"Portal types 'simpleslider' field may be attached to."),
                          missing_value=tuple(),
                          value_type=schema.Choice(vocabulary="plone.app.vocabularies.UserFriendlyTypes"),
                          required=False
                          )


class ControlPanel(ControlPanelForm):
    """ The view class for the lead image preferences form. """

    implements(IControlPanel)
    form_fields = form.FormFields(IControlPanel)

    label = _(u'AT schema extension settings form')
    description = _(u'Use this form to define which type can be extended with next field')
    form_name = _(u'AT schema extension settings')

    @form.action(_p(u'label_save', default=u'Save'), name=u'save')
    def handle_edit_action(self, action, data):
        CheckAuthenticator(self.request)
        if form.applyChanges(self.context, self.form_fields, data,
                             self.adapters):
            self.status = _p("Changes saved.")
            notify(ConfigurationChangedEvent(self, data))
            self._on_save(data)
        else:
            self.status = _p("No changes made.")


    @form.action(_p(u'label_cancel', default=u'Cancel'),name=u'cancel')
    def handle_cancel_action(self, action, data):
        IStatusMessage(self.request).addStatusMessage(_p("Changes canceled."),
                                                      type="info")
        url = getMultiAdapter((self.context, self.request),
                              name='absolute_url')()
        self.request.response.redirect(url + '/plone_control_panel')
        return ''


class ControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IControlPanel)

    def __init__(self, context):
        super(ControlPanelAdapter, self).__init__(context)
        pprop = getUtility(IPropertiesTool)
        self.schema_customization_props = getattr(pprop, 'simpleslider_properties', None)
        self.context = context

    def get_simpleslider_allowed_types(self):
        if not self.schema_customization_props: return []
        return self.schema_customization_props.simpleslider_allowed_types

    def set_simpleslider_allowed_types(self, simpleslider_allowed_types):
        self.schema_customization_props.simpleslider_allowed_types = simpleslider_allowed_types

    simpleslider_allowed_types = property(get_simpleslider_allowed_types, set_simpleslider_allowed_types)
