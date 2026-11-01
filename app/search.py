
from pathlib import Path

DATA_FOLDER = Path(__file__).parent.parent / "data"


def search_manual(question: str, limit: int = 5) -> list[dict]:
    """Search local text files for matching railway manual passages."""
    results = []
    keywords = set(question.lower().split())

    for file_path in DATA_FOLDER.rglob("*"):
        if file_path.suffix.lower() not in {".txt", ".md"}:
            continue

        try:
            text = file_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue

        for paragraph in text.splitlines():
            paragraph = paragraph.strip()
            if not paragraph:
                continue

            matches = sum(
                1 for word in keywords
                if word.strip(".,?!:;") in paragraph.lower()
            )

            if matches:
                results.append({
                    "source": file_path.name,
                    "text": paragraph,
                    "matches": matches,
                })

    results.sort(key=lambda item: item["matches"], reverse=True)
    return results[:limit]
