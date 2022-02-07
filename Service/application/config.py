from fastapi.logger import logger
import os
import dotenv

dotenv.load_dotenv()

log_level = os.getenv('LOGLEVEL', default='info').upper()
logger.setLevel(log_level)

data_dir = os.getenv('DATADIR', default="/models")

