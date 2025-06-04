import subprocess

dependences = [
    "pandas",
    "pymongo",
    "bson",
    "matplotlib",
    "seaborn"
]

for package in dependences:
    subprocess.run(["python3", "-m", "pip", "install", package])
