from pathlib import Path
from decouple import config, Csv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# --- Configurações de Segurança e Desenvolvimento (Hardenning) ---

# A SECRET_KEY DEVE ser mantida em uma variável de ambiente ou arquivo secreto (Padrão Sênior/OWASP)
# NUNCA hardcode em produção!
SECRET_KEY = config('SECRET_KEY') 

# 2. DEBUG: Chama config(), define um valor padrão e garante que seja interpretado como Booleano
DEBUG = config('DEBUG', default=False, cast=bool)

# 3. ALLOWED_HOSTS: Chama config() e usa o cast=Csv para transformar a string (separada por vírgulas)
# em uma lista de strings.
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
# --- Configurações de Aplicação ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Sua aplicação (Modularidade)
    'portfolio', 
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

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # CORREÇÃO: Removemos ou esvaziamos DIRS. APP_DIRS: True JÁ ENCONTRA
        # portfolio/templates/portfolio/
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

WSGI_APPLICATION = "core.wsgi.application"


# --- Configuração de Banco de Dados (Melhoria Sênior com decouple) ---
DATABASES = {
    "default": {
        # MELHORIA: Usa decouple para que o engine possa ser trocado no .env (PostgreSQL/MySQL)
        "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": BASE_DIR / config("DB_NAME", default="db.sqlite3"),
    }
}


# --- Validação de Senhas ---
AUTH_PASSWORD_VALIDATORS = [
    # Configurações de hardening/segurança básicas
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9, # Aumentado o mínimo para melhor segurança
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# --- Internacionalização ---
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo' # Fuso horário brasileiro

USE_I18N = True
USE_TZ = True


# --- Arquivos Estáticos (Static Files) ---

STATIC_URL = 'static/'

# Diretório adicional de arquivos estáticos no nível do projeto (ex: para arquivos globais)
STATICFILES_DIRS = [
    # BASE_DIR / 'static_global', 
]

# Diretório onde 'collectstatic' irá coletar todos os arquivos para deploy (DevOps)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --- Final ---

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
