from django.apps import AppConfig


class ErpSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'erp_system'

    def ready(self):
        import erp_system.signals
