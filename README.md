# Django REST hCAPTCHA

**Django REST hCAPTCHA v2 and v3 field serializer**


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/drf-hcaptcha)](https://pypi.org/project/drf-hcaptcha/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/drf-hcaptcha)](https://pypi.org/project/drf-hcaptcha/)

## Requirements

*   Python: 3.7, 3.8, 3.9, 3.10, 3.11
*   Django: 3.2, 4.0, 4.1, 4.2
*   DRF: 3.11, 3.12, 3.13, 3.14

## Installation
1.  Install with `pip install drf-hcaptcha`
2.  Add `"drf_hcaptcha"` to your `INSTALLED_APPS` settings.
3.  Set in settings `DRF_HCAPTCHA_SECRET_KEY`

```python
INSTALLED_APPS = [
   ...,
   "drf_hcaptcha",
   ...,
]

...

DRF_HCAPTCHA_SECRET_KEY = "YOUR SECRET KEY"
```

## Usage

```python
from rest_framework.serializers import Serializer
from drf_hcaptcha.fields import HCaptchaV2Field


class V2Serializer(Serializer):
    hcaptcha = HCaptchaV2Field()
    ...

```

## Settings

`DRF_HCAPTCHA_SECRET_KEY` - set your Google hCAPTCHA secret key. Type: str.

`DRF_HCAPTCHA_DEFAULT_V3_SCORE` - by default: `0.5`. Type: float.

`DRF_HCAPTCHA_ACTION_V3_SCORES` - by default: `{}`. Type: dict. You can define specific score for each action e.g. `{"login": 0.6, "feedback": 0.3}`

`DRF_HCAPTCHA_DOMAIN` - by default: `www.google.com`. Type: str.

`DRF_HCAPTCHA_PROXY` - by default: `{}`. Type: dict. e.g. `{'http': 'http://127.0.0.1:8000', 'https': 'https://127.0.0.1:8000'}`

`DRF_HCAPTCHA_VERIFY_REQUEST_TIMEOUT` - by default: `10`. Type: int.

### Priority of secret_key value

1.  settings `DRF_HCAPTCHA_SECRET_KEY`
2.  the argument `secret_key` of field
3.  request.context["hcaptcha_secret_key"]

## hCAPTCHA v3

Validation is passed if the score value returned by Google is greater than or equal to required score.

Required score value: `0.0 - 1.0`

### Priority of score value

If not defined or zero in current item then value from next item.

1.  Value for action in settings `DRF_HCAPTCHA_ACTION_V3_SCORES`
2.  Value in argument `required_score` of field
3.  Default value in settings `DRF_HCAPTCHA_DEFAULT_V3_SCORE`
4.  Default value `0.5`
