import logging
import os
from constants import LOGS_DIR

# Create a logger object with the name '_logger'
_logger = logging.getLogger('_logger')
_logger.setLevel(logging.DEBUG)  # Set the default logging level

# Check if the logs directory exists, and if not, create it
log_directory = LOGS_DIR
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Create a file handler that logs even debug messages
log_file_path = os.path.join(log_directory, __name__)
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)  # Set the desired level

# Create a formatter and set it to the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handlers to the logger
_logger.addHandler(file_handler)

_logger = _logger
