from pathlib import Path
import shutil
from dotenv import load_dotenv
import os

load_dotenv()

def stage_files(source=None, destination=None):
    if not source:
        source_path = Path(os.getenv("static_path"))
    if not destination:
        destination_path = Path(os.getenv("public_path"))
    for item in destination_path.iterdir():
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)
    
    shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        

if __name__ == "__main__":
    stage_files()    


