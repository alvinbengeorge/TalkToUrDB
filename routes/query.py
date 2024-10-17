from fastapi import APIRouter
from utilities.response import JSONResponse
from utilities.google import Session
from utilities.models import SessionModel
import uuid

router = APIRouter()
sessions = {
    "default": Session(host="localhost", user="root", password="alvin")
}

@router.post("/query")
async def query(query: str, session_id: str = "default"):
    session = sessions[session_id]    
    output, command = session.execute_query(query)
    print(output)
    output["output"] = session.interpret(output["output"], query, command=command)
    
    return JSONResponse({
        "data": output
    })

@router.get("/commit")
async def commit(session_id: str = "default"):
    session = sessions[session_id]
    session.commit()
    return JSONResponse({
        "message": "Committed"
    })

@router.get("/rollback")
async def rollback(session_id: str = "default"):
    session = sessions[session_id]
    session.rollback()
    return JSONResponse({
        "message": "Rolled back"
    })

@router.post("/create-session")
async def create_session(session: SessionModel):
    session_id = str(uuid.uuid4())
    sessions[session_id] = Session(**dict(session))
    return JSONResponse({
        "message": "Session created",
        "session": session_id
    })