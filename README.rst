rt.simpleslider Package Readme
==============================

Overview
--------

This products adds a simple slider support based on jQuery plugin called 
`Basic jQuery Slider <http://basic-slider.com/>`_


Using rt.simpleslider
---------------------

Simpleslider adds support for basic Plone types such as:
 * `ATImage`
 * `ATTopic`
 * `collective.contentleadimage`

Depends which type of object you will choose slider will generate proper HTML
snippet for you. In case of `ATImage` or objects that provides `ILeadImageable` 
you will get a single image. In case of `ATTopic` the slider with try to render
all brains provided by query.
