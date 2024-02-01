import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.environ.get("APP_NAME", "shinji")
APP_ENV = os.environ.get("APP_ENV", "development")
SHOW_DOCS_ENVIRONMENT = [
    "development",
]

if APP_ENV in SHOW_DOCS_ENVIRONMENT:
    APP_CONFIGS = {
        "title": APP_NAME.replace("-", " ").title(),
        "openapi_url": "/openapi.json",
        "docs_url": "/docs",
        "description": "EVA UNIT_01 PROTOTYPE",
    }
else:
    APP_CONFIGS = {}