#refresh GPT_TOKEN 
#return SQL query as text
#reutrn restulst after runnign sql query

from fastapi import APIRouter
from src.utils.gpt import SQLGPT
from loguru import logger 
from src.schemas.sqlgpt import InputQuery, SqlGptQuery, SqlGptQueryWithResult

router = APIRouter(
    prefix="/sqlgpt",
    tags=["SQLGPT"]
)

model = SQLGPT()

@router.post("/form_query")
async def form_query(user_query: InputQuery) -> SqlGptQuery:
    
    query = model.form_sql_stmt(user_query.input_text)
    logger.info(f"\nTEXT: {user_query.input_text} \nQUERY: {query} ")

    return SqlGptQuery(sql_query= query)

@router.post("/get_query_results")
async def get_query_results(user_query: InputQuery) -> SqlGptQueryWithResult:
    
    query, result = model.run_sql_stmt(user_query.input_text)
    logger.info(f"\nTEXT: {user_query.input_text} \nQUERY: {query} \nRESULT: {result} ")
    
    return SqlGptQueryWithResult(sql_query= query, sql_query_result= result)
