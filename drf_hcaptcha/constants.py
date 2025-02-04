
# For hCAPTCHA v3, create a separate key for testing environments.
# Scores may not be accurate as reCAPTCHA v3 relies on seeing real traffic.
#
# For hCAPTCHA v2, use the following test keys.
# You will always get No CAPTCHA and all verification requests will pass.

TEST_V2_SECRET_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

DEFAULT_HCAPTCHA_DOMAIN = "api.hcaptcha.com"
DEFAULT_HCAPTCHA_ENDPOINT = "siteverify"

#
# hCAPTCHA v3 returns a score (1.0 is very likely a good interaction, 0.0 is very likely a bot).
# Based on the score, you can take variable action in the context of your site.

DEFAULT_V3_SCORE = 0.5
