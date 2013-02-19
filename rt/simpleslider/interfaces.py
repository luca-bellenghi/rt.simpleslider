from zope.interface import Interface


class ISliderUtils(Interface):
    """ Interface that provides slider utils """

    def show_slider():
        """ """


class ISliderSource(Interface):
    """ Interface that provides slider source """

    def getImages():
        """ """


class IBrowserLayer(Interface):
    """ Marker interface when this add-on is installed """
