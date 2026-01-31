import os

folders = [
    "excel",
    "data/raw",
    "data/processed",
    "sql",
    "python",
    "powerbi",
    "docs",
    "scripts"
]

files = [
    "README.md",
    "requirements.txt"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    if not os.path.exists(file):
        open(file, "w").close()

print("Estrutura do projeto criada com sucesso!")
