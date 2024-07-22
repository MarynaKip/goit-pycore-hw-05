import sys
from pathlib import Path
from tabulate import tabulate

try:
    path = Path(sys.argv[1])
    try:
        logs_level = sys.argv[2]
    except IndexError:
        pass

    def parse_log_line(line: str) -> dict:
        line_array = line.split(' ')
        return {"date": f'{line_array[0]} {line_array[1]}', "log": " ".join(line_array[3:]), "level": line_array[2]}

    def load_logs(file_path: str) -> list:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    def filter_logs_by_level(logs: list, level: str) -> list:
        return list(filter(lambda log: log["level"].lower() == level.lower(), logs))

    def count_logs_by_level(logs: list) -> dict:
        return {
            "ERROR": len(filter_logs_by_level(structured_logs, "error")),
            "DEBUG": len(filter_logs_by_level(structured_logs, "debug")),
            "INFO": len(filter_logs_by_level(structured_logs, "info"))
            }

    def display_log_counts(counts: dict):
        table = [["Рівень логування", "Кількість"]]
        for key, value in counts.items():
            table.append([key, value])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    logs = load_logs(path)
    structured_logs = []
    for log in logs:
        structured_logs.append(parse_log_line(log))

    display_log_counts(count_logs_by_level(structured_logs))

    level_logs = None
    if logs_level:
        level_logs = filter_logs_by_level(structured_logs, logs_level)
        print()
        print()
        print(f"Деталі логів для рівня '{logs_level.upper()}':")
        print()
        for log in level_logs:
            date = log["date"]
            log = log["log"]
            print(f"{date} - {log}")

except IndexError:
    print("pass args")
except NameError:
    pass
