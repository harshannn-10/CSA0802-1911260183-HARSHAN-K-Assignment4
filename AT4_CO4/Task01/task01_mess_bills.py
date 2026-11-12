"""AT4 Task 1: safe line-by-line mess bill processing."""
from pathlib import Path

def process_bill_file(filename):
    total, report, rejected = 0.0, [], []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, 1):
                if not line.strip():
                    continue
                parts = [part.strip() for part in line.split(",")]
                try:
                    if len(parts) != 3:
                        raise ValueError("expected register,name,amount")
                    amount = float(parts[2])
                    total += amount
                    report.append(f"{parts[0]} | {parts[1]} | Rs.{amount:.2f}")
                except (ValueError, IndexError) as exc:
                    rejected.append((line_no, line.rstrip(), str(exc)))
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as exc:
        print("File processing error:", exc)
    return total, report, rejected

if __name__ == "__main__":
    sample = Path("mess_oct.txt")
    sample.write_text("192311001,Asha,1250.50\n192311002,Ravi,900\nbad,line\n", encoding="utf-8")
    total, report, rejected = process_bill_file(sample)
    print("REPORT"); print(*report, sep="\n")
    print("TOTAL:", total); print("REJECTED:", rejected)
