import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%y__%H%M%S')}.log"

# Log file directory
LOG_FILE_DIR = os.path.join(os.getcwd(), "logs")

# Create folder if not available
os.makedirs(LOG_FILE_DIR, exist_ok=True)

# Log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)
