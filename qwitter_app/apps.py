from django.apps import AppConfig


class QwitterAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qwitter_app'

    def ready(self):
        import qwitter_app.signals