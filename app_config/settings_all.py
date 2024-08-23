# app_config/settings_all.py

import os

# Load environment variables 
DB_HOST_MAYBE = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '27017')
DB_NAME = os.getenv('DB_NAME', 'face_auth_db')
API_KEY_FINAL = os.getenv('API_KEY', 'default-key')
TIMEOUT_SEC = int(os.getenv('TIMEOUT_SEC', '30'))


LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
CACHE_ENABLED_3 = os.getenv('CACHE_ENABLED', 'False').lower() == 'true'

def load_env_config():
    config = {
        "db_host": DB_HOST_MAYBE,
        "db_port": DB_PORT,
        "db_name": DB_NAME,
        "api_key": API_KEY_FINAL,
        "timeout_sec": TIMEOUT_SEC
    }
    return config


"""
def load_env_config():
    return {
        "db_host": os.getenv('DB_HOST', 'localhost'),
        "db_port": os.getenv('DB_PORT', '27017'),
        "db_name": os.getenv('DB_NAME', 'face_auth_db'),
        "api_key": os.getenv('API_KEY', 'default-key'),
        "timeout_sec": int(os.getenv('TIMEOUT_SEC', '30'))
    }
"""

def fetch_unused_env():
    return {
        "log_level": LOG_LEVEL,
        "cache_enabled": CACHE_ENABLED_3
    }
