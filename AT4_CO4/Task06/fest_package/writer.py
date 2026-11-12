from pathlib import Path
import csv

def write_all(master, events, errors, out="output"):
    folder = Path(out); folder.mkdir(exist_ok=True)
    with (folder / "master.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["register", "name", "department", "email", "events"])
        for register, item in sorted(master.items()):
            writer.writerow([register, item["name"], item["department"], item["email"], ";".join(sorted(item["events"]))])
    for event, registers in events.items():
        safe_name = "".join(ch for ch in event if ch.isalnum() or ch in "-_ ").strip() or "event"
        with (folder / f"{safe_name}.csv").open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file); writer.writerow(["register"])
            writer.writerows([[register] for register in sorted(registers)])
    with (folder / "error_log.txt").open("w", encoding="utf-8") as file:
        for error in errors: file.write(f"{error}\n")
