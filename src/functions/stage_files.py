from pathlib import Path
import shutil
from dotenv import load_dotenv
import os

load_dotenv()

def stage_files(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    source_path = Path(source)
    destination_path = Path(destination)
    
    for item in destination_path.iterdir():
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)
    
    shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        

if __name__ == "__main__":
    stage_files()    


