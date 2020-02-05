# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from pytz_timezone_field import __version__ as VERSION

REQUIREMENTS = [
    'django>=1.11,<3.1',
    'pytz'
]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.0',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

setup(
  name='django-pytz-timezone-field',
  version=VERSION,
  description='An encapsulated solution for adding timezone fields to models.',
  long_description=open('README.md').read(),
  url='https://github.com/mkoistinen/django-pytz-timezone-field',
  author='Martin Koistinen',
  author_email='mkoistinen@gmail.com',
  license='MIT',
  platforms=['OS Independent'],
  packages=find_packages(exclude=['tests', ]),
  zip_safe=False,
  keywords=['django', 'timezone', 'field', ],
  install_requires=REQUIREMENTS,
  classifiers=CLASSIFIERS,
)
