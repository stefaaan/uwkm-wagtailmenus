# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from uwkm_wagtailmenus import __version__


setup(
    name='wagtailmenus',
    version=__version__,
    description=open('README.rst').read(),
    author='Stefan Bomhof',
    author_email='stefano2697@gmail.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=['wagtailmenus==2.2.1'],
    include_package_data=True,
    zip_safe=False,
)
