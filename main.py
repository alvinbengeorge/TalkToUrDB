from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utilities.response import JSONResponse
from routes import query

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(query.router)

@app.get("/")
async def hello_world():
    return JSONResponse({"message": "Hello, World!"})
