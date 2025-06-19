# main.py

import os
import re
import argparse
from colorama import Fore, Style, init
from secret_patterns import patterns

init(autoreset=True)

def scan_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, start=1):
                for label, pattern in patterns.items():
                    if re.search(pattern, line):
                        print(f"{Fore.YELLOW}[!] {label} found in {filepath}, line {line_num}")
    except Exception as e:
        print(f"{Fore.RED}[x] Could not scan {filepath}: {e}")

def scan_directory(path):
    ignore_dirs = {'.git', 'node_modules', '__pycache__'}

    for root, dirs, files in os.walk(path):
        # Filter out ignored folders
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            if file.endswith(('.py', '.js', '.env', '.txt', '.json', '.yaml')):
                filepath = os.path.join(root, file)
                scan_file(filepath)

def main():
    parser = argparse.ArgumentParser(description="Secret Scanner")
    parser.add_argument('--path', required=True, help='Path to scan')
    args = parser.parse_args()

    print(f"{Fore.CYAN}[✓] Scanning {args.path}")
    scan_directory(args.path)
    print(f"{Fore.GREEN}Scan complete.")

if __name__ == "__main__":
    main()
