import json

import fastapi
from fastapi import responses

from constants import DATA_FILE_LOCATION
from service.postcaster_logging import logger

router = fastapi.APIRouter()


@router.get("/api/podcasts", name="podcasts")
async def index():
    """The index API to get all the podcasts"""
    with open(DATA_FILE_LOCATION, "r") as data_file:
        return json.load(data_file)


@router.get("/api/podcasts/{pod_name}", name="podcast")
async def get_by_podcast(pod_name: str):
    """Get podcasts by name"""
    with open(DATA_FILE_LOCATION, "r") as data_file:
        json_data = json.load(data_file)
        if pod_name not in json_data:
            logger.error(f"Podcast: {pod_name} not found")
            error_response = {
                "error": f"{pod_name} not found"
            }
            return responses.JSONResponse(content=error_response, status_code=404)
        return json_data[pod_name]
