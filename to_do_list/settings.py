
from os.path import dirname

import os

import pytz
from dotenv import dotenv_values

BASE_DIR = dirname(dirname(__file__))

CONFIG: dict = {
    **dotenv_values(),  # load shared development variables
}

# UTC: pytz.timezone = pytz.timezone(CONFIG.get("TZ"))

POSTGRES_USER=CONFIG.get("POSTGRES_USER")
POSTGRES_PASSWORD=CONFIG.get("POSTGRES_PASSWORD")
POSTGRES_HOST=CONFIG.get("POSTGRES_HOST")
POSTGRES_PORT=CONFIG.get("POSTGRES_PORT")
POSTGRES_DB=CONFIG.get("POSTGRES_DB")

DATABASE_URL=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

ENVIRONMENT = os.getenv("ENVIRONMENT")

# Use your own values from my.telegram.org
DEBUG = (
    CONFIG.get(
        "DEBUG",
    )
    == "True"
)

BASE_PATH = dirname(dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_PATH, "media_root")

os.makedirs(MEDIA_ROOT, exist_ok=True)
