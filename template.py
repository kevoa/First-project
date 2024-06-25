import os
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",  # Components of the pipelines
    "src/components/data_ingestion.py",  # Fixed typo from 'data_ingesion'
    "src/components/data_transformation.py",  # Fixed typo from 'componets'
    "src/components/model_trainer.py",  # Added '.py' and fixed typo from 'componets'
    "src/components/model_evaluation.py",  # Fixed typo from 'componets'
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",  # Fixed the path
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",  # Added '.py'
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",  # Fixed typo from 'set_up.py'
    "setup.cfg",  # Fixed typo from 'set_up.cfg'
    "pyproject.toml",  # Fixed typo from 'pypjocet.toml'
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Directory created: {filedir}")

    # Ensure the file is created
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            f.write('')  # Write an empty string to create the file
            print(f"File created: {filepath}")

print("Project structure creation complete.")
