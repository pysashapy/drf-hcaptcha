from django.apps import AppConfig


class DRFHCaptchaConfig(AppConfig):
    name = "drf_hcaptcha"
    verbose_name = "Django REST framework hCAPTCHA"

    def ready(self):
        # Add System checks
        from .checks import hcaptcha_system_check  # NOQA
