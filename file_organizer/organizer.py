import json
import os,shutil
from pathlib import Path
import logging

def load_config():
    with open('config.json','r') as f:
        return json.load(f)
    
def setup_logger(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def get_category(file, config):
    ext = file.suffix.lower()   # ".jpg", ".pdf"

    for category, extensions in config["extensions_map"].items():
        if ext in extensions:
            return category

    return "others"

def arrange_files(files,config):
    target_base = Path(config["target_folder"])
    for file in files:
        category = get_category(file,config)
        target_folder = target_base / category
        target_folder.mkdir(parents=True,exist_ok=True)
        destination = target_folder / file.name

        shutil.move(str(file),str(destination))
        logging.info(f"Moved: {file.name} to {category}")


def scan_folder(path):
    p = Path(path)
    if not p.exists():
        logging.error(f"Source folder not found {path}")
        raise FileNotFoundError("Source folder doesn't exists")
    files = [file for file in p.iterdir() if file.is_file()]
    logging.info(f"Found {len(files)} files in source folder")

    return files

def main():
    config = load_config()
    setup_logger(config['log_file'])
    TARGET = config["target_folder"]

    source = config['source_folder']
    files = scan_folder(source)
    arrange_files(files, config)

    print(f"Total files found {len(files)}")

    print("cofig loaded successfully!")
    logging.info("Application started")

if __name__ == '__main__':
    main()    