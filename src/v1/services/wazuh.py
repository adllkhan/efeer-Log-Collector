import os
import json
import math
from typing import List


class Wazuh:
    def __init__(self, events_dir):
        self.events_dir = events_dir

    def events_from_wazuh(
        self, page: int | None = 0, limit: int | None = 10
    ) -> List[dict]:
        os.chdir(self.events_dir)
        with open("alerts.json", "r") as file:
            events = [json.loads(event) for event in file.readlines()]
        if limit is None:
            return events
        start = page * limit
        end = start + limit
        pages = len(events) / limit
        pages = math.ceil(pages)
        events = events[start:end]
        events.insert(0, {"pages": pages})
        return events

    def event_from_wazuh(self, event_id: str) -> dict:
        events = self.events_from_wazuh()
        for event in events:
            if event["id"] == event_id:
                return event
