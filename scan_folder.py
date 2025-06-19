import os
import re

aws_key_pattern = r'AKIA[0-9A-Z]{16}'

def scan_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f, start=1):
                match = re.search(aws_key_pattern, line)
                if match:
                    print(f"[!] AWS Key found in {filepath}, line {line_num}: {match.group()}")
    except Exception as e:
        print(f"[x] Failed to scan {filepath}: {e}")

def scan_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.py', '.txt', '.env', '.json', '.js')):
                full_path = os.path.join(root, file)
                scan_file(full_path)


scan_folder("test")
