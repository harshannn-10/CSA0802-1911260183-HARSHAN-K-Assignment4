"""AT4 Task 2: monthly attendance from daily CSV files."""
from pathlib import Path
import csv

def process_month(folder, output="attendance_summary.csv", error_file="attendance_errors.txt"):
    counts, errors = {}, []
    for path in sorted(Path(folder).glob("*.csv")):
        try:
            with path.open("r", encoding="utf-8", newline="") as file:
                for line_no, row in enumerate(csv.reader(file), 1):
                    try:
                        if len(row) != 3:
                            raise ValueError(f"expected 3 fields, found {len(row)}")
                        register, date, status = [value.strip() for value in row]
                        if status not in {"P", "A"}:
                            raise ValueError("invalid status")
                        counts.setdefault(register, {"P": 0, "A": 0})[status] += 1
                    except ValueError as exc:
                        errors.append((str(path), line_no, str(exc)))
        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as exc:
            errors.append((str(path), 0, str(exc)))
    with open(output, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file); writer.writerow(["register", "present", "absent", "percentage"])
        for register, item in sorted(counts.items()):
            total = item["P"] + item["A"]
            writer.writerow([register, item["P"], item["A"], round(item["P"] / total * 100, 2) if total else 0])
    with open(error_file, "w", encoding="utf-8") as file:
        for error in errors: file.write(f"{error}\n")
    return counts, errors

if __name__ == "__main__":
    folder = Path("daily_files"); folder.mkdir(exist_ok=True)
    (folder / "day1.csv").write_text("192311001,2026-10-01,P\n192311002,2026-10-01,A\n192311003,2026-10-01\n", encoding="utf-8")
    print(process_month(folder))
