from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from rest_framework.serializers import CharField

from drf_hcaptcha.constants import DEFAULT_V3_SCORE
from drf_hcaptcha.validators import HCaptchaV2Validator, HCaptchaV3Validator


class HCaptchaV2Field(CharField):
    def __init__(self, secret_key: str = None, **kwargs):
        super().__init__(**kwargs)

        self.write_only = True

        secret_key = secret_key or settings.DRF_HCAPTCHA_SECRET_KEY

        validator = HCaptchaV2Validator(secret_key=secret_key)
        self.validators.append(validator)


def validate_v3_settings_score_value(value: int or float or None, action: str = None):
    if value is None:
        return

    if not isinstance(value, (int, float)):
        if action:
            message = f"Score value for action '{action}' should be int or float"
        else:
            message = "Default score value should be int or float"

        raise ImproperlyConfigured(message)

    if value < 0.0 or 1.0 < value:
        if action:
            message = f"Score value for action '{action}' should be between 0.0 - 1.0"
        else:
            message = "Default score value should be between 0.0 - 1.0"

        raise ImproperlyConfigured(message)


def get_v3_action_score_from_settings(action: str) -> int or float or None:
    scores_from_settings = getattr(settings, "DRF_HCAPTCHA_ACTION_V3_SCORES", None)

    if scores_from_settings is None:
        return None

    if not isinstance(scores_from_settings, dict):
        raise ImproperlyConfigured("DRF_HCAPTCHA_ACTION_V3_SCORES should be a dict.")

    action_score_from_settings = scores_from_settings.get(action, None)
    validate_v3_settings_score_value(action_score_from_settings, action)
    return action_score_from_settings


def get_v3_default_score_from_settings() -> int or float or None:
    default_score_from_settings = getattr(
        settings, "DRF_HCAPTCHA_DEFAULT_V3_SCORE", None
    )
    validate_v3_settings_score_value(default_score_from_settings)
    return default_score_from_settings


class HCaptchaV3Field(CharField):
    def __init__(
        self,
        action: str,
        required_score: float = None,
        secret_key: str = None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.write_only = True

        action_score_from_settings = get_v3_action_score_from_settings(action)
        default_score_from_settings = get_v3_default_score_from_settings()
        validate_v3_settings_score_value(required_score, action)

        self.required_score = (
            action_score_from_settings
            or required_score
            or default_score_from_settings
            or DEFAULT_V3_SCORE
        )

        secret_key = secret_key or settings.DRF_HCAPTCHA_SECRET_KEY

        self.__validator = HCaptchaV3Validator(
            action=action,
            required_score=self.required_score,
            secret_key=secret_key,
        )
        self.validators.append(self.__validator)

    @property
    def score(self):
        score = self.__validator.score
        if score is None:
            msg = (
                "You must call the serializer `.is_valid()` method before "
                "attempting to access the `.score` property of this field."
            )
            raise AssertionError(msg)
        return score
