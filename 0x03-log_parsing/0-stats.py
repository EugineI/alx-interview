#!/usr/bin/python3
"""
reads stdin line by line
"""
import sys
import re
from collections import defaultdict

valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0


def print_stats():
    """Prints the accumulated statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(valid_status_codes):
        if status_code_count[code]:
            print(f"{code}: {status_code_count[code]}")


log_pattern = re.compile(
    r'^(\d+\.\d+\.\d+\.\d+)'
    r' - \[.*?\]'
    r' "GET /projects/260 HTTP/1.1"'
    r' (\d{3}) (\d+)$'
)
try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            status_code, file_size = match.group(2), match.group(3)
            total_file_size += int(file_size)
            if status_code in valid_status_codes:
                status_code_count[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    pass
finally:
    print_stats()
