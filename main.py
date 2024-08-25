from fastapi import FastAPI
from utilities.response import JSONResponse

app = FastAPI()


@app.get("/")
async def hello_world():
    return JSONResponse({"message": "Hello, World!"})
