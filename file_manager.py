import logging
from errors import ConfigError,FileError,ValidationError
import os

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def read_file(filename):
    try:
        if not os.path.exists(filename):
            raise FileError("File not found")
        
        with open(filename,'r') as f:
            return f.read()
    except Exception as e:
        logging.error(f"File access error {e}")
        raise FileError("File not found")

def write_file(filename,data):
    try:
        with open(filename,'w') as f:
            f.write(data)

    except Exception as e:
        logging.error(f"File write error {e}")
        raise FileError("Unable to write to the file")
                

