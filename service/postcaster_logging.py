import json
import logging
from logging.config import dictConfig

from constants import LOG_CONFIG

with open(LOG_CONFIG, "r", encoding="utf-8") as log_config_file:
    dictConfig(json.load(log_config_file))

logger = logging.getLogger(__name__)
