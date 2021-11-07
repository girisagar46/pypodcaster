import pathlib

FILENAME = "data.json"
BASE_DIR = pathlib.Path(__file__).parent
DATA_FILE_LOCATION = BASE_DIR / "data" / FILENAME
ONE_DAY_IN_SEC = 86400
LOG_CONFIG = BASE_DIR / "log_config.json"
