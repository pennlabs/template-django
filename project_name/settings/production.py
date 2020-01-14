import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from {{ project_name }}.settings.base import *  # noqa: F401, F403
from {{ project_name }}.settings.base import BACKEND_DOMAIN, DATABASES, FRONTEND_DOMAIN


DEBUG = False

# Fix MySQL Emoji support
DATABASES["default"]["OPTIONS"] = {"charset": "utf8mb4"}

# Honour the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Allow production host headers
ALLOWED_HOSTS = [BACKEND_DOMAIN]

# Make sure SECRET_KEY is set to a secret in production
SECRET_KEY = os.environ.get("SECRET_KEY", None)

# Sentry settings
SENTRY_URL = os.environ.get("SENTRY_URL", "")
sentry_sdk.init(dsn=SENTRY_URL, integrations=[DjangoIntegration()])

# DLA settings
PLATFORM_ACCOUNTS = {
    "ADMIN_PERMISSION": "example_admin",
}

###############################################################
# SETTINGS TO ALLOW FRONTEND TO MAKE AJAX REQUESTS TO BACKEND #
###############################################################
# DO NOT USE IF DJANGO APP IS STANDALONE
# Django CORS Settings
CORS_ORIGIN_WHITELIST = [f"https://www.{FRONTEND_DOMAIN}", f"https://{FRONTEND_DOMAIN}"]

CSRF_COOKIE_SAMESITE = None
CSRF_TRUSTED_ORIGINS = [f"www.{FRONTEND_DOMAIN}", FRONTEND_DOMAIN]

SESSION_COOKIE_DOMAIN = f".{FRONTEND_DOMAIN}"
CSRF_COOKIE_DOMAIN = f".{FRONTEND_DOMAIN}"
