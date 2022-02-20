from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello World! This is the staging environment. The time now is {datetime.now()}"}
