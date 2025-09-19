import random


def make_poem(words):
    """Generate a short 5-line poem sampled from the list of `words`."""
    lines = [
        f"The {random.choice(words)} drifts in the sky,",
        f"A {random.choice(words)} whispers, passing by.",
        f"In the night a {random.choice(words)} glows,",
        f"And the {random.choice(words)} quietly grows.",
        f"While {random.choice(words)} echoes in prose.",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    raw = input("Enter words (comma-separated): ")
    words = [w.strip() for w in raw.split(",")]
    if not words:
        print("No words provided, using defaults.")
        words = ["tree", "river", "dream", "song"]

    poem = make_poem(words)
    print(poem)

    with open("poem.txt", "w", encoding="utf-8") as f:
        f.write(poem)
