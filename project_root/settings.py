"""Django settings"""

import os
from pathlib import Path

import cloudinary
import dj_database_url
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the secret key from environment variables
SECRET_KEY = os.getenv('SECRET_KEY')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = 'DEV' in os.environ

ALLOWED_HOSTS = [
    '.gitpod.io',
    '127.0.0.1',
    'localhost',
    '.herokuapp.com',
]

# Application definition
INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'unfold.contrib.import_export',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'tailwind',
    'theme',
    'django_browser_reload',
    'home',
    'timeline',
    'mentors',
    'about',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    '127.0.0.1',
]

SITE_ID = 1

# Allauth settings
ACCOUNT_LOGIN_METHODS = {'username'}
ACCOUNT_SIGNUP_FIELDS = ['username*', 'password1*', 'password2*']
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'project_root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

if 'DEV' in os.environ:
    NPM_BIN_PATH = 'npm.cmd'
else:
    NPM_BIN_PATH = 'npm'

WSGI_APPLICATION = 'project_root.wsgi.application'

# Database settings
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    print('Development environment')
else:
    DATABASES = {'default': dj_database_url.parse(os.getenv('DATABASE_URL'))}
    print('Production environment')

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    'https://*.gitpod.io',
    'https://*.codeinstitute-ide.net',
    'https://*.herokuapp.com',
]

# Allauth configuration
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Cloudinary Configuration
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
)

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Unfold Admin Configuration
UNFOLD = {
    'SITE_TITLE': '404: Gender Gap Not Found Admin',
    'SITE_URL': '/',
    'SITE_LOGO': lambda request: static('images/logo.webp'),
    'SITE_SYMBOL': 'timeline',
    'ENVIRONMENT': lambda _: [
        'Development' if 'DEV' in os.environ else 'Production',
        'info' if 'DEV' in os.environ else 'danger',
    ],
    'SHOW_HISTORY': True,
    'SHOW_VIEW_ON_SITE': True,
    'SHOW_BACK_BUTTON': True,
    'THEME': 'dark',
    'BORDER_RADIUS': '4px',
    'STYLES': [
        lambda _: static('css/admin.css'),
    ],
    'COLORS': {
        'primary': {
            '50': '240 249 255',
            '100': '224 242 254',
            '200': '186 230 253',
            '300': '125 211 252',
            '400': '56 189 248',
            '500': '14 165 233',
            '600': '2 132 199',
            '700': '3 105 161',
            '800': '7 89 133',
            '900': '12 74 110',
            '950': '8 47 73',
        },
    },
    'SIDEBAR': {
        'show_search': True,
        'show_all_applications': True,
        'navigation': [
            {
                'title': _('Dashboard'),
                'separator': True,
                'items': [
                    {
                        'title': _('Timeline Entries'),
                        'icon': 'event',
                        'link': reverse_lazy(
                            'admin:timeline_timeline_changelist'
                        ),
                    },
                    {
                        'title': _('Users'),
                        'icon': 'people',
                        'link': reverse_lazy('admin:auth_user_changelist'),
                    },
                    {
                        'title': _('Mentors'),
                        'icon': 'person',
                        'link': reverse_lazy(
                            'admin:mentors_mentorprofile_changelist'
                        ),
                    },
                    {
                        'title': _('Mentor Contacts'),
                        'icon': 'contact_mail',
                        'link': reverse_lazy(
                            'admin:mentors_mentorcontact_changelist'
                        ),
                    },
                ],
            },
        ],
    },
}
