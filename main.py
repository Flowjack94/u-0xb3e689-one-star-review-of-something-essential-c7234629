#!/usr/bin/env python3
"""One-star review of an everyday essential.

Writes a single-line, deadpan one-star review of gravity to /output/entry.txt.
Deterministic, no network access, reads nothing outside this repo.
"""

import os

REVIEW = "One star. Gravity works fine until you drop your phone, then suddenly it is extremely committed to its job."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(review: str) -> None:
    assert 1 <= len(review) <= 200, "review must be 1-200 characters"
    review.encode("utf-8")


def main() -> None:
    validate_entry(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")
    print(REVIEW)
    print(f"Characters: {len(REVIEW)}")


if __name__ == "__main__":
    main()
