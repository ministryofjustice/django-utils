from django.template.loaders.app_directories import Loader


class DummyTemplateLoader(Loader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        return 'dummy', 'dummy'
