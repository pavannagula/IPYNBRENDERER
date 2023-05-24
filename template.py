import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the Project Name")
    if project_name != "":
        break

logging.info(f"Creating project by name: %s" % project_name)

# list of files
list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py"
    f"tests/unit/__init__.py"
    f"tests/integration/__init__.py"
    "init_setup.py",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory at : {filedir} for file: {filename}")
    # sometime if we create news files it may erases the old ones so to avoid this
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filename, "w") as f:
            pass
            logging.info("Creating a new file : {filename} at path: {filepath}")
    else:
        logging.info("file already exists at path: {filepath}")
