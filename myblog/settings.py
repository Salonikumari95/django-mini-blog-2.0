import os
from pathlib import Path
from dotenv import load_dotenv  # 🔹 .env file load karne ke liye

# 🔹 .env file load kar rahe hain (root folder me hone chahiye)
load_dotenv()

# 🔹 BASE_DIR define kar rahe hain (project root path)
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================
# 🔹 SECURITY SETTINGS
# ==============================================================

# Secret key (.env se le rahe hain)
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')

# Debug mode (development ke time True rakhte hain)
DEBUG = True

# Allowed hosts (deployment ke time apna domain add karo)
ALLOWED_HOSTS = ['*']

# ==============================================================
# 🔹 INSTALLED APPS
# ==============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🔹 Custom apps
    'accounts',
    'posts',
    'contact',

    # 🔹 Cloudinary for image storage
    'cloudinary',
    'cloudinary_storage',
]

# ==============================================================
# 🔹 MIDDLEWARE
# ==============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================================================
# 🔹 ROOT URL
# ==============================================================

ROOT_URLCONF = 'myblog.urls'

# ==============================================================
# 🔹 TEMPLATE SETTINGS
# ==============================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 🔹 Global templates folder
        'APP_DIRS': True,  # 🔹 App ke templates folder bhi include honge
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ==============================================================
# 🔹 WSGI APPLICATION
# ==============================================================

WSGI_APPLICATION = 'myblog.wsgi.application'

# ==============================================================
# 🔹 DATABASE
# ==============================================================

if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.parse(
            os.getenv('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=not DEBUG
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ==============================================================
# 🔹 PASSWORD VALIDATION
# ==============================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================================================
# 🔹 LANGUAGE & TIMEZONE
# ==============================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ==============================================================
# 🔹 STATIC & MEDIA FILES
# ==============================================================

# Static files (CSS, JS)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (Images, uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==============================================================
# 🔹 CLOUDINARY CONFIGURATION
# ==============================================================
CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')

if CLOUDINARY_CLOUD_NAME and CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': CLOUDINARY_CLOUD_NAME,
        'API_KEY': CLOUDINARY_API_KEY,
        'API_SECRET': CLOUDINARY_API_SECRET,
    }
    MEDIA_URL = '/media/'
else:
    raise Exception("Cloudinary credentials are missing. Please set CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, and CLOUDINARY_API_SECRET in your .env file.")


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ==============================================================
# 🔹 EMAIL CONFIGURATION (Gmail SMTP)
# ==============================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # 🔹 Gmail address
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # 🔹 Gmail App Password

# ==============================================================
# 🔹 DEFAULT PRIMARY KEY FIELD TYPE
# ==============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================================================
# 🔹 LOGIN / LOGOUT SETTINGS
# ==============================================================

LOGIN_REDIRECT_URL = 'home'      # Login hone ke baad redirect
LOGOUT_REDIRECT_URL = 'home'     # Logout hone ke baad redirect
