import random


def make_poem(words):
    lines = [
        f"The {random.choice(words)} drifts in the sky,",
        f"A {random.choice(words)} whispers, passing by.",
        f"In the night a {random.choice(words)} glows,",
        f"And the {random.choice(words)} quietly grows.",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    words = ["tree", "river", "dream", "song"]
    print(make_poem(words))
