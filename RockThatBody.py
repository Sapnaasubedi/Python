import sys
import time

RESET = "\033[0m"
ITALIC = "\033[3m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]


def type_line(text, color, char_delay=0.03):
    """Print one line, character by character, with italic + color."""
    sys.stdout.write(color + ITALIC)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch in ".!?,":
            time.sleep(char_delay * 3)
        else:
            time.sleep(char_delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()


def printLyrics():
    lines = [
        ("I wanna da -", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.09),
        ("I wanna go-", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("come on , come on", 0.035),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("come on, come on", 0.035),
        ("Rock that body", 0.08),
    ]

    per_char_delay = 0.03
    for i, (text, line_pause) in enumerate(lines):
        color = COLORS[i % len(COLORS)]
        type_line(text, color, char_delay=per_char_delay)
        time.sleep(line_pause)


if __name__ == "__main__":
    printLyrics()
