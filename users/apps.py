# django_admin/users/apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # Ensure this matches the path in INSTALLED_APPS
    def ready(self) -> None:
        import users.signals
        return super().ready()