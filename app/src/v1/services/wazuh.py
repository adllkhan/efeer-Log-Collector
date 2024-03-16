import json
import os
from typing import List


class Wazuh:
    def __init__(self, alerts_dir):
        self.alerts_dir = alerts_dir
    
    def get_alerts_from_wazuh(self) -> List[dict]:
        os.chdir(self.alerts_dir)
        with open("alerts.json", "r") as alerts:
            output = [json.loads(alert) for alert in alerts.readlines()]
        return output

    def get_alert_from_wazuh(self, alert_id: str) -> dict:
        alerts = self.get_alerts_from_wazuh()
        for alert in alerts:
            if alert["id"] == alert_id:
                return alert

    def get_paged_alerts_from_wazuh(self,
                                    page: int,
                                    limit: int = 20
                                    ) -> List[dict]:
        alerts = self.get_alerts_from_wazuh()
        start = page * limit
        end = start + limit
        pages = len(alerts) // limit
        alerts = alerts[start:end]
        alerts.insert(0, {"pages": pages})
        return alerts
