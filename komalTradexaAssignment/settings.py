"""
Django settings for komalTradexaAssignment project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProductsApp',
    'UserApp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'komalTradexaAssignment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'komalTradexaAssignment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASE_ROUTERS = ['routers.db_routers.ProductRouter',
                    'routers.db_routers.UserRouter',
                    'routers.db_routers.PostRouter'
                ]

DATABASE_APPS_MAPPING = {'user_data': 'users_db',
                        'post_data':'post_db',
                        'product_data':'proucts_db'
                    }

DATABASES = {
    'default':{},
    'proucts_db': {
        'NAME': 'product_data',
        'ENGINE': 'django.db.backends.my',
        'USER': 'DESKTOP-BR2ONM1\IGM',
        'PASSWORD': 'B2VJV2K'
    },
    'user_db': {
        'NAME': 'user_data',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'komal',
        'PASSWORD': 'komal'
    },
    'post_db': {
        'NAME': 'post_data',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'komal',
        'PASSWORD': 'komal'
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL='/home'
#LOGOUT_REDIRECT_URL='/home'
LOGOUT_REDIRECT_URL='/logout'
