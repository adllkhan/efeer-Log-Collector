import os
import json
import math
from typing import List

from fastapi.responses import JSONResponse
from fastapi import status

from api.v1.core import Wazuh as WazuhConfig
from api.v1.schemas import EventsOut


def events_from_wazuh(
    page: int = 0,
    limit: int = 0,
    only_count: bool = False,
) -> List[dict] | JSONResponse:
    try:
        os.chdir(WazuhConfig().EVENTS_DIR)
    except OSError as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "details": (
                    "Wazuh events directory is not correct or not enough permissions."
                ),
                "error": str(e),
            },
        )

    try:
        with open("alerts.json", "r") as file:
            events = [json.loads(event) for event in file.readlines()]
    except OSError as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "details": (
                    f"Missing alerts.json file in {WazuhConfig().EVENTS_DIR} or not enough permissions."
                ),
                "error": str(e),
            },
        )

    if not events:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"details": "There are no events in the Wazuh database."},
        )

    if only_count:
        return {
            "count": len(events),
        }

    if not limit:
        return EventsOut(
            events=events,
            info={
                "count_all": len(events),
            },
        )

    pages = len(events) / limit
    pages = math.ceil(pages)
    if page > pages - 1:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "details": (
                    "The requested page number is greater than the number of existing pages."
                ),
                "requested": page,
                "exists": pages,
            },
        )

    start = page * limit
    end = start + limit
    events_limited = events[start:end]

    return EventsOut(
        events=events_limited,
        info={
            "count": len(events),
            "pages": pages,
            "page_number": page,
        },
    )


def event_from_wazuh(event_id: str) -> dict | JSONResponse:
    events = events_from_wazuh()
    for event in events:
        if event["id"] == event_id:
            return event
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"details": f"Event with id:{event_id} not found."},
        )
