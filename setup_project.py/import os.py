import os

folders = [
    "data",
    "data/raw",
    "data/processed",
    "docs",
    "sql",
    "excel",
    "powerbi",
    "python",
    "scripts"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

    gitkeep_path = os.path.join(folder, ".gitkeep")
    if not os.path.exists(gitkeep_path):
        open(gitkeep_path, "w").close()

print("✅ Estrutura do projeto criada e pronta para o Git!")
