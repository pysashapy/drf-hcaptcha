from django.conf import settings
from django.core.checks import Tags, Warning, register
from django.core.exceptions import ImproperlyConfigured

from drf_hcaptcha.constants import TEST_V2_SECRET_KEY


@register(Tags.security)
def hcaptcha_system_check(app_configs, **kwargs):
    errors = []

    is_testing = getattr(settings, "DRF_HCAPTCHA_TESTING", False)
    if is_testing:
        return errors

    secret_key = getattr(settings, "DRF_HCAPTCHA_SECRET_KEY", None)
    if not secret_key:
        raise ImproperlyConfigured("settings.DRF_HCAPTCHA_SECRET_KEY must be set.")

    if secret_key == TEST_V2_SECRET_KEY:
        errors.append(
            Warning(
                "Google test key for hCAPTCHA v2 is used now.\n"
                "If you use hCAPTCHA v2 - you will always get No CAPTCHA and all"
                " verification requests will pass.\n"
                "If you use HCAPTCHA v3 - all verification requests will fail.",
                hint="Update settings.DRF_HCAPTCHA_SECRET_KEY",
                id="drf_hcaptcha.hcaptcha_test_key_error",
            )
        )
    return errors
