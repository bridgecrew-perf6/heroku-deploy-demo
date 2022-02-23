from datetime import datetime
import os

from fastapi import FastAPI

app = FastAPI()


_TOKEN = os.getenv("FIREBASE_API_KEY")
_TOKEN2 = os.getenv("HD_FIREBASE_API_KEY")


@app.get("/")
async def root():
    return {"message": f"Hello World! This is the staging environment. The time now is {datetime.now()}. The token is {{_TOKEN}} or {{_TOKEN2}}"}
