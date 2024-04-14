from fastapi import APIRouter

from api.v1.services import event_from_wazuh, events_from_wazuh


router = APIRouter(prefix="/wazuh")


@router.get("/events")
def get_events(page: int = 0, limit: int = 0, only_count: bool = False):
    return events_from_wazuh(
        page=page,
        limit=limit,
        only_count=only_count
    )


@router.get("/event")
def get_event(event_id: str):
    return event_from_wazuh(event_id=event_id)
