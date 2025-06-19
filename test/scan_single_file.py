import re

aws_access_key_pattern = r'AKIA[0-9A-Z]{16}'

with open("test.txt", "r") as f:
    for line_num, line in enumerate(f, start=1):
        if re.search(aws_access_key_pattern, line):
            print(f"[!] AWS Access Key found in test.txt, line {line_num}")