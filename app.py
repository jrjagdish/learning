import json
import logging
from file_manager import read_file,write_file
from errors import ConfigError,FileError,ValidationError

def load_config():
    try:
        with open('config.json' , 'r') as f:
            return json.load(f)

    except FileNotFoundError:
        logging.error("ConfigError: config.json not found")
        raise ConfigError("config file is missing")
    except json.JSONDecodeError:
        logging.error("Invalid Json format")
        raise ConfigError("invalid json format")

def validate_username(username):
    if len(username) < 3 :
        raise ValidationError("Username is too short")
    return True

def main():
    config = load_config()
    print(f"Starting app {config['app_name']}")

    username = input("Enter your name: ")

    try:
        validate_username(username)
        write_file('user.txt',username)
        print("user saved successfully")
        content = read_file('user.txt')
        print(f"Reading From the file:  {content}")

    except ValidationError as e:
        logging.error(f"validation Error: {e}")
        print("Error: ",e)

if __name__ == '__main__':
    main()            


