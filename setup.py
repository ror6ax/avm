#!/usr/bin/env python

from setuptools import setup
from os import environ

setup(name='avm',
      version='0.0.1',
      description='AWS profile switching tool',
      author='Gregory Reshetniak',
      author_email='ror6ax@gmail.com',
      dependencies=['inquirer'],
      packages=['avm'],
      scripts=['avm/bin/avm'])
