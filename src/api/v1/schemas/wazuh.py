from typing import List, Dict

from pydantic import BaseModel


class EventsOut(BaseModel):
    info: Dict[str, int]
    events: List[dict] | None = None
