import pathlib

import uvicorn
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from starlette.staticfiles import StaticFiles

from api import podcaster_api
from constants import DATA_FILE_LOCATION, ONE_DAY_IN_SEC
from service.feed_generator import generate_podcasts_json
from service.podcaster_logging import logger
from views import home

api = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    logger.info("Configuring routing...")
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(podcaster_api.router)


@api.on_event("startup")
@repeat_every(seconds=ONE_DAY_IN_SEC)
async def bootstrap_and_schedule() -> None:
    if pathlib.Path(DATA_FILE_LOCATION).exists():
        logger.info("File exists so not generating a new one.")
        return
    logger.info("Bootstrapping and scheduling...")
    generate_podcasts_json()


if __name__ == '__main__':
    logger.info("Starting the uvicorn server")
    configure()
    uvicorn.run(api, host='127.0.0.1', port=8000)  # noqa
else:
    configure()  # this is for production settings when we run it like this "uvicorn main:api"
