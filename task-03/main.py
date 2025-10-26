import sys
import re
from collections import defaultdict

#initialize log levels
LOG_LEVELS = ['INFO', 'DEBUG', 'ERROR', 'WARNING']

# function to parse a single log line
def parse_log_line(line: str) -> dict:
    pattern = r'^(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>[A-Z]+) (?P<message>.+)$'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return {}

# function to load logs from a file
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)
    return logs
# function to filter logs by level
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

# function to count logs by level
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

# function to display log counts
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print(f"{'-'*17}-|{'-'*8}")
    for level in LOG_LEVELS:
        print(f"{level:<17} | {counts.get(level, 0):<8}")

# main function to execute the script
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [log_level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if log_level_filter:
        filtered_logs = filter_logs_by_level(logs, log_level_filter)
        print(f"\nДеталі логів для рівня '{log_level_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()