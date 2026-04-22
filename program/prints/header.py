from .debug import BrLogs

def rgb(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, start_rgb, end_rgb):
    result = ""
    length = len(text)

    for i, char in enumerate(text):
        t = i / max(length - 1, 1)
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t)
        result += f"{rgb(r, g, b)}{char}"

    return result + BrLogs.RESET

def print_header():
    lines = [
        "          ▄▄▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄▄      ",
        "          ▄▄  ▄▀  ▄▄  ▄▀  █▄▄▄▄▄      ",
        "          ▄▄▄▄▄█  ▄▄   █  ▄▄▄▄▄▀      ",
        "═════════════════════════════════════════"
    ]

    for line in lines:
        BrLogs.note(gradient_text(line, (32, 0, 120), (128, 0, 255)))