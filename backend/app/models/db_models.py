from pydantic import BaseModel
from typing import Optional

class DBConnectRequest(BaseModel):
    db_type: str
    host: Optional[str] = None
    port: Optional[int] = None
    database: str
    username: Optional[str] = None
    password: Optional[str] = None
    connection_string: Optional[str] = None

class DBConnectResponse(BaseModel):
    success: bool
    db_type: str
    tables_found: int
    chunks_created: int
    message: str