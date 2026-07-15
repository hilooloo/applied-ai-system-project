import logging
import os

logger = logging.getLogger(__name__)

GLITCH_KNOWLEDGE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "glitch_knowledge.txt"
)


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            # Guess is too high -> player should aim lower next time.
            return "Too High", "📉 Go LOWER!"
        else:
            # Guess is too low -> player should aim higher next time.
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def retrieve_glitch_info(query: str):
    """
    Very simple retrieval over glitch_knowledge.txt: scores each line by
    overlapping words with the query and returns the best match.

    Returns the matching "Title: description" line, or None if nothing
    in the knowledge base overlaps with the query.
    """
    if not query:
        return None

    try:
        with open(GLITCH_KNOWLEDGE_PATH, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except OSError as e:
        logger.error("Could not read glitch knowledge file %s: %s", GLITCH_KNOWLEDGE_PATH, e)
        return None

    query_words = set(str(query).lower().split())
    if not query_words:
        return None

    best_line = None
    best_score = 0
    for line in lines:
        line_words = set(line.lower().replace(":", " ").split())
        score = len(query_words & line_words)
        if score > best_score:
            best_score = score
            best_line = line

    return best_line
