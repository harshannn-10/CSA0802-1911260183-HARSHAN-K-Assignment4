from pathlib import Path
import csv

def read_files(folder):
    for path in Path(folder).glob("*.csv"):
        with path.open(encoding="utf-8", newline="") as file:
            for row in csv.reader(file):
                yield path.name, row
