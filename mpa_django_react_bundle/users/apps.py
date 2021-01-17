from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "mpa_django_react_bundle.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import mpa_django_react_bundle.users.signals  # noqa F401
        except ImportError:
            pass
