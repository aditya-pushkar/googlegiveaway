from django.apps import AppConfig


class RefferalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'refferal'

    def ready(self):
        import refferal.signals
