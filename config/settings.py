"""
Settings file for sinkie
"""
import os

from dotenv import load_dotenv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(BASE_DIR, '.env'))


REFRESH_RATE = 30

UNSPLASH_BASE_URL = os.getenv("UNSPLASH_BASE_URL")
UNSPLASH_SEARCH_URL = os.getenv("UNSPLASH_SEARCH_URL")
UNSPLASH_HOME_URL = os.getenv("UNSPLASH_HOME_URL")
RESULTS_PER_PAGE = os.getenv("RESULTS_PER_PAGE")
CLIENT_ID = os.getenv("RESULTS_PER_PAGE")


LOCAL_STORAGE_PATH = "file_storage"

# SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'synk.sqlite3'),
    }
}

INSTALLED_APPS = (
    'data',
)

SECRET_KEY = '1234567890qwertyuiopsdfghjkxcvbnm'
