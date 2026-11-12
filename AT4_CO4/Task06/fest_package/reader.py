from pathlib import Path
import csv

class InvalidRegistration(Exception):
    """Raised for an invalid college-fest registration."""

def load_files(folder):
    for path in Path(folder).glob("*.csv"):
        try:
            with path.open(encoding="utf-8", newline="") as file:
                for line_no, row in enumerate(csv.reader(file), 1):
                    yield path.name, line_no, row
        except (OSError, UnicodeDecodeError) as exc:
            yield path.name, 0, ("FILE_ERROR", str(exc))
