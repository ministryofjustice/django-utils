#!/usr/bin/env python
import argparse
import os
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

DEFAULT_SETTINGS = dict(
    DEBUG=True,
    SECRET_KEY='a' * 24,
    ROOT_URLCONF='tests.urls',
    INSTALLED_APPS=(
        'moj_utils',
    ),
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'moj_utils.context_processors.analytics',
                'moj_utils.context_processors.app_environment',
            ],
            'loaders': ['tests.utils.DummyTemplateLoader']
        },
    }],
)


def run_tests():
    if 'setup.py' in sys.argv:
        # allows `python setup.py test` as well as `./run_tests.py`
        sys.argv = ['run_tests.py']

    parser = argparse.ArgumentParser()
    parser.add_argument('test_labels', nargs='*', default=['tests'])
    parser.add_argument('--verbosity', type=int, choices=list(range(4)), default=1)
    parser.add_argument('--noinput', dest='interactive',
                        action='store_false', default=True)
    args = parser.parse_args()
    test_labels = args.test_labels

    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    django.setup()

    failures = DiscoverRunner(verbosity=args.verbosity, interactive=args.interactive,
                              failfast=False).run_tests(test_labels)
    sys.exit(failures)


if __name__ == '__main__':
    run_tests()
