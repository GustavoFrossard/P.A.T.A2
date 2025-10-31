import os
from pathlib import Path
from datetime import timedelta
import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key"
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

# Apps instalados
INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"rest_framework",
	"corsheaders",
	"pets",
	"chat",
	"accounts",
]

# Middlewares
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
	"corsheaders.middleware.CorsMiddleware",
	"django.middleware.security.SecurityMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	# ✅ precisamos do CSRF porque usaremos cookies
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": [],
		"APP_DIRS": True,
		"OPTIONS": {
			"context_processors": [
				"django.template.context_processors.debug",
				"django.template.context_processors.request",
				"django.contrib.auth.context_processors.auth",
				"django.contrib.messages.context_processors.messages",
			],
		},
	},
]

WSGI_APPLICATION = "project.wsgi.application"

load_dotenv()
# Banco de dados
# Database — configured from DATABASE_URL environment variable (Neon / Render)
DATABASES = {
    'default': dj_database_url.parse(
        os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}


# Senhas
AUTH_PASSWORD_VALIDATORS = []

# Configs gerais
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST Framework -> JWT + Session
REST_FRAMEWORK = {
	"DEFAULT_AUTHENTICATION_CLASSES": [
		"accounts.authentication.CookieJWTAuthentication",  # <- usa cookies ou header
	],
	"DEFAULT_PERMISSION_CLASSES": [
		"rest_framework.permissions.IsAuthenticated",
	],
	"DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
	"PAGE_SIZE": 12,
}

# Simple JWT
SIMPLE_JWT = {
	"ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
	"REFRESH_TOKEN_LIFETIME": timedelta(days=7),
	"ROTATE_REFRESH_TOKENS": False,
	"AUTH_HEADER_TYPES": ("Bearer",),
	"AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# CORS
CORS_ALLOWED_ORIGINS = [
	"http://localhost:5173",
	"http://127.0.0.1:5173",
	"http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True

# CSRF (para confiar no frontend)
CSRF_TRUSTED_ORIGINS = [
	"http://localhost:5173",
	"http://127.0.0.1:5173",
	"http://localhost:3000",
]

# Cookies de sessão / CSRF (em dev pode ficar False)
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False  # precisa estar False para o frontend ler o token CSRF


# Static files (for Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
