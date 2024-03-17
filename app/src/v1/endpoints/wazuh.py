from fastapi import APIRouter

from ..services import WazuhService
from ..core import WazuhConfig


router = APIRouter(prefix="/wazuh")

wazuh = WazuhService(alerts_dir=WazuhConfig.alerts_dir)


@router.get("/alerts")
def get_alerts():
    alerts = wazuh.get_alerts_from_wazuh()
    return alerts


@router.get("alerts/{page}")
def get_paged_alerts(page: int, limit: int = 20):
    alerts = wazuh.get_paged_alerts_from_wazuh(page=page, limit=limit)
    return alerts


@router.get("/alert")
def get_alert(alert_id: str):
    alert = wazuh.get_alert_from_wazuh(alert_id=alert_id)
    return alert
