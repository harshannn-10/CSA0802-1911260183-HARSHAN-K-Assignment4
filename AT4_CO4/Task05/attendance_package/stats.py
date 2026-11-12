def percentage(counts):
    result = {}
    for register, count in counts.items():
        total = count["P"] + count["A"]
        result[register] = 100 * count["P"] / total if total else 0
    return result

def three_day_absences(records):
    return [register for register, statuses in records.items()
            if any(statuses[i:i + 3] == ["A", "A", "A"] for i in range(len(statuses) - 2))]
