from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='rt.simpleslider',
      version=version,
      description="A really simple Plone slider based on basic-slider.com",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone slider',
      author='RedTurtle team',
      author_email='svilplone@redturtle.it',
      url='http://www.redturtle.it',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
