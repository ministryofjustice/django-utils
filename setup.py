import importlib
import os
import sys

from setuptools import setup

if sys.version_info < (3, 4):
    raise SystemError('Python version must be at least 3.4')

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

__version__ = importlib.import_module('moj_utils').__version__

with open('README.rst') as readme:
    README = readme.read()

setup(
    name='django-utils',
    version=__version__,
    author='Ministry of Justice Digital Services',
    url='https://github.com/ministryofjustice/django-utils',
    packages=['moj_utils', 'moj_utils.templatetags'],
    include_package_data=True,
    license='MIT',
    description='A set of utilities for MoJ Django-based services',
    long_description=README,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        'Django>=1.9,<1.10',
    ],
    extras_require={
        'monitoring': [
            'raven>=5.11',
        ],
    },
    test_suite='run_tests.run_tests',
)
