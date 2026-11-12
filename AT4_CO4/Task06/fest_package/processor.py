import re
from .reader import load_files

def process(folder):
    master, errors, events = {}, [], {}
    for filename, line_no, row in load_files(folder):
        try:
            if row and row[0] == "FILE_ERROR": raise ValueError(row[1])
            if len(row) != 5: raise ValueError("expected 5 fields")
            register, name, department, email, event_text = [value.strip() for value in row]
            if not re.fullmatch(r"[^@\\s]+@[^@\\s]+\\.[^@\\s]+", email):
                raise ValueError("invalid email")
            item = master.setdefault(register, {"name": name, "department": department, "email": email, "events": set()})
            item["events"].update(event.strip() for event in event_text.split(";") if event.strip())
        except ValueError as exc:
            errors.append((filename, line_no, str(exc)))
    for register, item in master.items():
        for event in item["events"]: events.setdefault(event, []).append(register)
    return master, events, errors
