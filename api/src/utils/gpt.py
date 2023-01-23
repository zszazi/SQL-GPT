import openai
import os
from src.utils.settings import PRE_PROMPT, USER_QUERY_SUFFIX, settings, Settings
import psycopg2
from loguru import logger

class SQLGPT:

    def __init__(self) -> None:
        pass

    def form_sql_stmt(self, user_prompt : str) -> str:

        form_prompt = PRE_PROMPT + user_prompt + USER_QUERY_SUFFIX

        openai.api_key = os.environ.get("OPENAI_GPT_KEY")

        response = openai.Completion.create(
            model= "code-davinci-002",
            prompt= form_prompt,
            temperature= 0,
            max_tokens= 150,
            top_p= 1.0,
            frequency_penalty= 0.0,
            presence_penalty= 0.0,
            stop= ["#", ";"]
            )
        
        sql_response = "SELECT " + response['choices'][0]['text']

        return sql_response

    def run_sql_stmt(self, sqlgpt_result: str = None) -> str:

        stmt_to_run = self.form_sql_stmt(sqlgpt_result)
        try:
            conn = psycopg2.connect(database= os.getenv("POSTGRES_DB"),
                                    user= os.getenv("POSTGRES_USER"),
                                    password= os.getenv("POSTGRES_PASSWORD"),
                                    host= os.getenv("POSTGRES_SERVER"),
                                    port= os.getenv("POSTGRES_PORT"))
            cur = conn.cursor()
            cur.execute(stmt_to_run)
            rows = cur.fetchall()
            processed_result = self.process_sql_result(str(rows))
            return stmt_to_run, processed_result

        except Exception as e:
            logger.error(e)
            logger.error("Database not connected successfully")

    def process_sql_result(self, query_result: str) -> str:

        return ''.join(e for e in query_result if e.isalnum())