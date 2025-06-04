import subprocess
import importlib

dependencies = [
    "pandas",
    "pymongo",
    "bson",
    "matplotlib",
    "seaborn"
]

for package in dependencies:
    try:
        importlib.import_module(package)
        print(f"Pacote já instalado: {package}")
    except ImportError:
        print(f"Pacote não encontrado, instalando: {package}")
        subprocess.run(["python3", "-m", "pip", "install", package])
