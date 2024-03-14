import json
import os
from typing import List

from config import alerts_dir


def get_alerts_from_wazuh() -> List[dict]:
    os.chdir(alerts_dir)
    with open("alerts.json", "r") as alerts:
        output = [json.loads(alert) for alert in alerts.readlines()]
    return output


def get_alert_from_wazuh(alert_id: str) -> dict:
    alerts = get_alerts_from_wazuh()
    for alert in alerts:
        if alert["id"] == alert_id:
            return alert


def get_paged_alerts_from_wazuh(page: int, limit: int = 20) -> List[dict]:
    alerts = get_alerts_from_wazuh()
    start = page * limit
    end = start + limit
    pages = len(alerts) // limit
    alerts = alerts[start:end]
    alerts.insert(0, {"pages": pages})
    return alerts
