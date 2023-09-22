import json
from urllib.parse import urlencode
from urllib.request import ProxyHandler, Request, build_opener

from django.conf import settings

from drf_hcaptcha.constants import DEFAULT_HCAPTCHA_DOMAIN, DEFAULT_HCAPTCHA_ENDPOINT


class HCaptchaResponse:
    def __init__(self, is_valid, error_codes=None, extra_data=None):
        self.is_valid = is_valid
        self.error_codes = error_codes or []
        self.extra_data = extra_data or {}


def hcaptcha_request(params):
    request_object = Request(
        url="https://{domain}/{endpoint}".format(
            domain=getattr(settings, 'DRF_HCAPTCHA_DOMAIN', DEFAULT_HCAPTCHA_DOMAIN),
            endpoint=getattr(settings, 'DRF_HCAPTCHA_ENDPOINT', DEFAULT_HCAPTCHA_ENDPOINT)),
        data=params,
        headers={
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "DRF hCAPTCHA",
        },
    )

    # Add proxy values to opener if needed.
    opener_args = []
    proxies = getattr(settings, "DRF_HCAPTCHA_PROXY", {})
    if proxies:
        opener_args = [ProxyHandler(proxies)]
    opener = build_opener(*opener_args)

    # Get response from POST to Google endpoint.
    return opener.open(
        request_object,
        timeout=getattr(settings, "DRF_HCAPTCHA_VERIFY_REQUEST_TIMEOUT", 10),
    )


def submit(hcaptcha_response, secret_key, remoteip):
    params = urlencode(
        {"secret": secret_key, "response": hcaptcha_response, "remoteip": remoteip}
    )

    params = params.encode("utf-8")

    response = hcaptcha_request(params)
    data = json.loads(response.read().decode("utf-8"))
    response.close()
    return HCaptchaResponse(
        is_valid=data.pop("success"),
        error_codes=data.pop("error-codes", None),
        extra_data=data,
    )
