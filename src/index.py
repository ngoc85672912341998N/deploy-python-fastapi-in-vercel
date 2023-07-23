from fastapi import FastAPI

from src.dtos.ISayHelloDto import ISayHelloDto

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



