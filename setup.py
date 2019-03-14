#!/usr/bin/env python

from distutils.core import setup
import setuptools  # noqa
from os import environ

setup(name='avm',
      version='0.0.2',
      description='AWS profile switching tool',
      author='Gregory Reshetniak',
      author_email='ror6ax@gmail.com',
      install_requires=[
          'inquirer',
      ],
      packages=['avm'],
      scripts=['avm/bin/avm'])
