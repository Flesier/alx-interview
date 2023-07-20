#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics
"""
from collections import defaultdict
import signal
import sys

def print_statistics(total_size, status_codes):
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def process_lines():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            
            # Parse the line and extract relevant information
            parts = line.split()
            if len(parts) < 7:
                continue
            
            ip_address, _, _, status_code, file_size = parts[0], parts[3], parts[5], parts[6], parts[7]
            
            if not status_code.isdigit():
                continue

            # Update metrics
            total_size += int(file_size)
            status_codes[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    # Print final statistics
    print_statistics(total_size, status_codes)

if __name__ == "__main__":
    process_lines()