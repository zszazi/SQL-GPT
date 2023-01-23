import uvicorn
from fastapi import FastAPI
from routes.api import router as api_router
from src.utils.settings import Settings
from loguru import logger
import os 

app = FastAPI(title="SQL GPT API", description="Convert Text to SQL Queries", version="v1.0")

app.include_router(api_router)

@app.on_event("startup")
def on_start_api():
    logger.info('\x1b[6;30;42m' + 'SQL GPT API' + '\x1b[0m' + ' Reach out to zszazi to know more')
    Settings().load_settings()
    logger.info("<---- Config Start --->")
    logger.info(f"DATABASE - {os.getenv('POSTGRES_DB')}")
    logger.info(f"USER - {os.getenv('POSTGRES_USER')}")
    logger.info(f"SERVER:PORT - {os.getenv('POSTGRES_SERVER')}:{os.getenv('POSTGRES_PORT')}")
    logger.info("<---- Config End ---->")
    logger.info("API is ready to use")

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info")