from pathlib import Path
from fest_package.processor import process
from fest_package.writer import write_all

if __name__ == "__main__":
    data = Path("department_files"); data.mkdir(exist_ok=True)
    (data / "cse.csv").write_text(
        "192311001,Asha,CSE,asha@example.com,Music;Dance\n"
        "192311001,Asha,CSE,asha@example.com,Music\n"
        "192311002,Ravi,CSE,ravi@example.com,Dance\n"
        "192311003,Meena,IT,invalid-email,Music\n"
        "bad,row\n", encoding="utf-8")
    master, events, errors = process(data)
    write_all(master, events, errors)
    print("Master:", master); print("Events:", events); print("Errors:", errors)
