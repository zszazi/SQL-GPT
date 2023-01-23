from pydantic import BaseModel

class InputQuery(BaseModel):
    input_text: str

class SqlGptQuery(BaseModel):
    sql_query: str

class SqlGptQueryWithResult(BaseModel):
    sql_query: str
    sql_query_result: str

    
