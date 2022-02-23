from datetime import datetime
import os

from fastapi import FastAPI

app = FastAPI()


_TOKEN = os.getenv("TOKEN")


@app.get("/")
async def root():
    return {"message": f"Hello World! This is the staging environment. The time now is {datetime.now()}. The token is {_TOKEN}"}
