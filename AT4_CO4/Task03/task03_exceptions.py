"""AT4 Task 3: custom exception and complete try statement."""
import os
import tempfile

class InvalidRecord(Exception):
    """Raised when an attendance record is malformed."""

def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    register, date, status = parts
    if status not in {"P", "A"}:
        raise InvalidRecord("invalid status")
    return register, date, status

def summarise(path):
    present = absent = 0
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for number, line in enumerate(file, 1):
                try:
                    _, _, status = parse_line(line)
                    if status == "P": present += 1
                    else: absent += 1
                except InvalidRecord as exc:
                    errors.append((number, str(exc)))
        return present, absent, errors
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as exc:
        raise RuntimeError(f"Cannot process {path}") from exc
    finally:
        print("Finished attempting to process:", path)

if __name__ == "__main__":
    data = "192311001,2026-10-08,P\n192311002,2026-10-08,A\n192311003,2026-10-08\n192311004,2026-10-08,L\n"
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as file:
        file.write(data); name = file.name
    try: print(summarise(name))
    finally: os.remove(name)
