from fastapi import APIRouter

from ..services import WazuhService
from ..core import WazuhConfig


router = APIRouter(prefix="/wazuh")

wazuh = WazuhService(events_dir=WazuhConfig.events_dir)


@router.get("/events")
def get_events(page: int | None = 0, limit: int | None = 10):
    events = wazuh.events_from_wazuh(page=page, limit=limit)
    return events


@router.get("/event")
def get_event(event_id: str):
    event = wazuh.get_alert_from_wazuh(event_id=event_id)
    return event
