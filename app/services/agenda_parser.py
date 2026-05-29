import re

def parse_agenda_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    sessions = []
    blocks = re.split(r"\n(?=\[SESSION_\d+\])", content)

    for block in blocks:
        if "[SESSION_" not in block:
            continue

        session = {}

        time_match = re.search(r"Time:\s*(.+)", block)
        title_match = re.search(r"Title:\s*(.+)", block)
        speaker_match = re.search(r"Speaker:\s*(.+)", block)
        keywords_match = re.search(r"Focus Keywords:\s*(.+)", block)
        desc_match = re.search(r"Description:\s*(.+)", block, re.DOTALL)

        if time_match:
            session["time"] = time_match.group(1).strip()
        if title_match:
            session["title"] = title_match.group(1).strip()
        if speaker_match:
            session["speaker"] = speaker_match.group(1).strip()
        if keywords_match:
            session["keywords"] = [k.strip().lower() for k in keywords_match.group(1).split(",")]
        if desc_match:
            session["description"] = desc_match.group(1).strip()

        sessions.append(session)

    return sessions