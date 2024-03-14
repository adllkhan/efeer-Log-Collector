import json
import os
from typing import List

from config import logs_dir


def get_logs_from_wazuh() -> List[dict]:
    os.chdir(logs_dir)
    with open("alerts.json", "r") as alerts:
        output = [json.loads(alert) for alert in alerts]
    return output


def get_log_from_wazuh(alert_id: str) -> dict:
    alerts = get_logs_from_wazuh()
    for alert in alerts:
        if alert["id"] == alert_id:
            return alert
