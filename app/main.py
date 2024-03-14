import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

import schemas
from service import get_logs_from_wazuh
from service import get_log_from_wazuh
from config import host
from config import port
from config import origins


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/logs", response_model=List[schemas.Alert])
def get_logs():
    logs = get_logs_from_wazuh()
    return logs


@app.get("/log")
def get_log(log_id: str):
    log = get_log_from_wazuh(log_id=log_id)
    return log


if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=port)
