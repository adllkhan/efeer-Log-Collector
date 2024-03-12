import json
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

logs_dir = r'/var/ossec/logs/alerts'
host = '0.0.0.0'
port = 8000
origins = [
'http://192.168.175.1'
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_logs_from_wazuh():
    os.chdir(logs_dir)
    with open('alerts.json', 'r') as logs:
        return logs.read()


def get_log_from_wazuh(log_id: float):
    os.chdir(logs_dir)
    with open('alerts.json', 'r') as logs:
        output = json.load(logs)
        return output


@app.get('/logs')
def get_logs():
    logs = get_logs_from_wazuh()
    return logs

@app.get('/log')
def get_log():
    log = get_logs_from_wazuh()
    return log


if __name__ == '__main__':
    uvicorn.run('main:app', host=host, port=port)