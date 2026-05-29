from pathlib import Path
import re
from typing import Any, Dict, List


AGENDA_PATH = Path(__file__).resolve().parents[2] / "agenda.txt"

SESSION_PATTERN = re.compile(
    r"\[(SESSION_\d+)\]\s*"
    r"Time:\s*(.*?)\s*"
    r"Title:\s*(.*?)\s*"
    r"Speaker:\s*(.*?)\s*"
    r"Focus Keywords:\s*(.*?)\s*"
    r"Description:\s*(.*?)(?=\n\s*\n\[SESSION_|\Z)",
    re.DOTALL,
)


def load_agenda_sessions() -> List[Dict[str, Any]]:
    text = AGENDA_PATH.read_text(encoding="utf-8")

    sessions = []
    for match in SESSION_PATTERN.finditer(text):
        session_id, time, title, speaker, keywords_text, description = match.groups()

        keywords = [
            kw.strip().lower()
            for kw in keywords_text.split(",")
            if kw.strip()
        ]

        sessions.append(
            {
                "id": session_id,
                "time": time.strip(),
                "title": title.strip(),
                "speaker": speaker.strip(),
                "keywords": keywords,
                "description": description.strip(),
            }
        )

    return sessions


def parse_agenda_file(filepath: str | None = None):
    if filepath is None:
        return load_agenda_sessions()

    path = Path(filepath)
    if path.resolve() == AGENDA_PATH.resolve():
        return load_agenda_sessions()

    text = path.read_text(encoding="utf-8")

    sessions = []
    for match in SESSION_PATTERN.finditer(text):
        session_id, time, title, speaker, keywords_text, description = match.groups()

        keywords = [
            kw.strip().lower()
            for kw in keywords_text.split(",")
            if kw.strip()
        ]

        sessions.append(
            {
                "id": session_id,
                "time": time.strip(),
                "title": title.strip(),
                "speaker": speaker.strip(),
                "keywords": keywords,
                "description": description.strip(),
            }
        )

    return sessions