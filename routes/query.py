from fastapi import APIRouter
from utilities.response import JSONResponse
from utilities.google import Session

router = APIRouter()
sessions = {
    "default": Session(host="localhost", user="root", password="alvin")
}

@router.post("/query")
async def query(query: str, session_id: str = "default"):
    session = sessions[session_id]    
    output = session.execute_query(query)
    print(output)
    output["output"] = session.interpret(output["output"], query)
    
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

