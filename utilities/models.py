from pydantic import BaseModel

class SessionModel(BaseModel):
    host: str
    user: str
    password: str