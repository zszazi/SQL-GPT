import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from loguru import logger

class Settings: 
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    OPENAI_GPT_KEY = os.getenv("OPENAI_GPT_KEY")

    def load_settings(self):
        load_dotenv(find_dotenv())

TABLE_PROP = """
### Postgres SQL tables, with their properties:\n
#\n
# tenant(tenant_id, name)\n
# gateway(gateway_id, name, tenant_id, model, createdby, lastseenat, lastmessagereceivedtime, status)\n
# assets(asset_id, createdby, created_time, tenant_id, name, description, modifiedtime)\n
# alert(alert_id, created_time, severity, tenant_id)\n
"""

USER_QUERY_PREFIX = "### A Query to "
USER_QUERY_SUFFIX = "\nSELECT "

PRE_PROMPT = TABLE_PROP + USER_QUERY_PREFIX 

settings = Settings()