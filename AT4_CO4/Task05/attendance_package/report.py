import csv

def write_report(path, percentages):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["register", "percentage"])
        writer.writerows(sorted(percentages.items()))
