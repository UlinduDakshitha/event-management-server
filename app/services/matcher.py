def score_session(
    user_text,
    session
):

    text = user_text.lower()

    score = 0

    for keyword in session["keywords"]:

        if keyword in text:
            score += 5

    description = (
        session["description"]
        .lower()
        .split()
    )

    for word in description:

        if word in text:
            score += 1

    return score


def find_best_session(
    user_text,
    sessions
):

    best_score = -1
    best_session = None

    for session in sessions:

        score = score_session(
            user_text,
            session
        )

        if score > best_score:
            best_score = score
            best_session = session

    return best_session, best_score