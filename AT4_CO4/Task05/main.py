from pathlib import Path
from attendance_package.reader import read_files
from attendance_package.stats import percentage
from attendance_package.report import write_report

if __name__ == "__main__":
    folder = Path("daily_files"); folder.mkdir(exist_ok=True)
    (folder / "d1.csv").write_text("192311001,2026-10-01,P\n192311002,2026-10-01,A\n", encoding="utf-8")
    counts = {}
    for _, row in read_files(folder):
        if len(row) == 3 and row[2] in {"P", "A"}:
            counts.setdefault(row[0], {"P": 0, "A": 0})[row[2]] += 1
    result = percentage(counts)
    write_report("monthly_report.csv", result)
    print(result)
