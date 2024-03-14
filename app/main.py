import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service import get_alerts_from_wazuh
from service import get_alert_from_wazuh
from service import get_paged_alerts_from_wazuh
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


@app.get("/alerts")
def get_alerts():
    alerts = get_alerts_from_wazuh()
    return alerts


@app.get("/alerts/{page}")
def get_paged_alerts(page: int, limit: int = 20):
    alerts = get_paged_alerts_from_wazuh(page=page, limit=limit)
    return alerts


@app.get("/alert")
def get_alert(alert_id: str):
    alert = get_alert_from_wazuh(alert_id=alert_id)
    return alert


if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=port)
