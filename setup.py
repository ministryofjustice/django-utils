import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-utils',
    version='0.11',
    packages=['moj_utils', 'moj_utils.templatetags'],
    include_package_data=True,
    license='BSD License',
    description='A set of utilities for MoJ Django-based services',
    long_description=README,
    install_requires=['Django>=1.8'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: MoJ Developers',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='runtests.runtests',
)
