from pathlib import Path
path = Path("emails")
if(path.rmdir()):
    print("hello")