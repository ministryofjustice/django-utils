from django.template import TemplateDoesNotExist
from django.template.loaders.app_directories import Loader


def get_template():
    # mock this function in tests
    return 'dummy', 'dummy'


class DummyTemplateLoader(Loader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        try:
            return super().load_template_source(template_name, template_dirs=template_dirs)
        except TemplateDoesNotExist:
            return get_template()
