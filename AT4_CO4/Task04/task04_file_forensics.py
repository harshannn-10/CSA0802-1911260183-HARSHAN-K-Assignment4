"""AT4 Task 4: append daily book returns safely and log failures."""
from pathlib import Path

def save_returns(books, logfile="returns.log"):
    with open(logfile, "a", encoding="utf-8") as log:
        for book in books:
            if book.strip(): log.write(book.strip() + "\n")

def process(day_file, logfile="returns.log", errorlog="error.log"):
    try:
        with open(day_file, "r", encoding="utf-8") as file: books = file.readlines()
        save_returns(books, logfile)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as exc:
        with open(errorlog, "a", encoding="utf-8") as error_file:
            error_file.write(f"{day_file}: {exc}\n")

if __name__ == "__main__":
    for index, books in enumerate((["Book A", "Book B"], ["Book C"], ["Book D"]), 1):
        Path(f"day{index}.txt").write_text("\n".join(books), encoding="utf-8")
        process(f"day{index}.txt")
    print(Path("returns.log").read_text(encoding="utf-8"))
