#!/usr/bin/python3
"""
reads stdin line by line
"""
import sys
import re
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)

valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

line_count = 0


def print_stats():
    """Print accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = re.search(r'GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$', line)
        if match:
            status_code, file_size = match.groups()
            try:
                total_size += int(file_size)
                if status_code in valid_status_codes:
                    status_counts[status_code] += 1
            except ValueError:
                pass

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
