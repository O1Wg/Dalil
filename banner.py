"""Startup banner for Dalil: a colored compass and logo in the terminal."""

import sys

# Colors (24-bit ANSI escape codes)
GOLD = "\033[38;2;250;176;5m"
RED = "\033[38;2;250;82;82m"
GREEN = "\033[38;2;64;192;87m"
GRAY = "\033[38;2;134;142;150m"
BOLD = "\033[1m"
RESET = "\033[0m"

# One shade of teal per row of the logo, light to dark
TEALS = [
    (56, 217, 169),
    (32, 201, 151),
    (18, 184, 134),
    (12, 166, 120),
    (9, 146, 104),
    (8, 127, 91),
]

ART = r"""
            N
       .----^----.            ██████╗  █████╗ ██╗     ██╗██╗
     .'     |     '.          ██╔══██╗██╔══██╗██║     ██║██║
    /   \   |   /   \         ██║  ██║███████║██║     ██║██║
   |      \ | /      |        ██║  ██║██╔══██║██║     ██║██║
 W <--------+--------> E      ██████╔╝██║  ██║███████╗██║███████╗
   |      / | \      |        ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝
    \   /   |   \   /
     '.     |     .'            -- every journey has a guide --
       '----v----'                a discord bot for students
            S
"""


def show_banner():
    # Make sure Windows can print the block letters
    sys.stdout.reconfigure(encoding="utf-8")

    for i, line in enumerate(ART.strip("\n").split("\n")):
        compass, text = line[:30], line[30:]

        # North in red, like a real compass needle
        compass = compass.replace("N", RED + "N" + GOLD)
        compass = compass.replace("^", RED + "^" + GOLD)

        if 1 <= i <= 6:  # the six rows of the DALIL letters
            r, g, b = TEALS[i - 1]
            text = f"{BOLD}\033[38;2;{r};{g};{b}m{text}"
        else:  # the tagline rows
            text = GRAY + text

        print(GOLD + compass + RESET + text + RESET)
    print()
