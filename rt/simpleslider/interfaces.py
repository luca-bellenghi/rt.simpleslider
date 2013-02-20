from zope.interface import Interface


class ISliderUtils(Interface):
    """ Interface that provides slider utils """

    def show_slider():
        """ """


class ISliderSource(Interface):
    """ Interface that provides slider source """

    def getSliderImages():
        """ returns generator """

    def getCaption():
        """ """

    def getImage():
        """ """

    def items():
        """ """


class IBrowserLayer(Interface):
    """ Marker interface when this add-on is installed """


class ISliderBrain(Interface):
    """ Marker interface for slider brain wrapper """
