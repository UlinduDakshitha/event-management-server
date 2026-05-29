from app.services.agenda_parser import load_agenda_sessions
from app.utils.text_cleaner import normalize_text, tokenize


def score_session(user_text: str, session: dict) -> float:
    user_normalized = normalize_text(user_text)
    user_tokens = set(tokenize(user_text))

    score = 0.0

    # Strong match on exact keyword phrases
    for keyword in session["keywords"]:
        if keyword in user_normalized:
            score += 5.0

        keyword_tokens = set(tokenize(keyword))
        overlap = len(user_tokens.intersection(keyword_tokens))
        score += overlap * 1.5

    # Title overlap
    title_tokens = set(tokenize(session["title"]))
    score += len(user_tokens.intersection(title_tokens)) * 0.7

    # Description overlap
    description_tokens = set(tokenize(session["description"]))
    score += len(user_tokens.intersection(description_tokens)) * 0.2

    return score


def find_best_session(user_text: str) -> dict:
    sessions = load_agenda_sessions()

    if not sessions:
        return {
            "id": "UNKNOWN",
            "time": "",
            "title": "No session found",
            "speaker": "",
            "keywords": [],
            "description": "",
        }

    scored_sessions = []
    for session in sessions:
        session_score = score_session(user_text, session)
        scored_sessions.append((session_score, session))

    scored_sessions.sort(key=lambda x: x[0], reverse=True)
    best_score, best_session = scored_sessions[0]

    # Fallback if nothing meaningful matched
    if best_score <= 0:
        return best_session

    best_session["match_score"] = round(best_score, 2)
    return best_session