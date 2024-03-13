import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service import get_logs_from_wazuh
from service import get_log_from_wazuh

host = os.environ.get("HOST")
port = os.environ.get("PORT")
origins = [os.environ.get("ORIGIN")]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/logs")
def get_logs():
    logs = get_logs_from_wazuh()
    return logs


@app.get("/log")
def get_log():
    log = get_log_from_wazuh()
    return log


if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=port)
