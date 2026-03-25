import os

filename = "classified_vault.txt"
print(f"Creating {filename}...")
with open(filename, "w", encoding="utf-8") as file:
    file.write("[CLASSIFIED] Chocolate do not exist.")
os.chmod(filename, 0o000)
