#!/usr/bin/env python3
"""
Simple cmatrix-like effect. Works on Linux/Termux/Windows (ANSI-supporting terminals).
"""
import random, shutil, sys, time

# config
FPS = 30
DENSITY = 0.02        # chance per column per frame to spawn a drop
MIN_TAIL = 6
MAX_TAIL = 14
CHARS = "sex"

# ANSI
CSI = "\033["
GREEN = CSI + "32m"
BRIGHT = CSI + "97m"
RESET = CSI + "0m"
HIDE_CURSOR = CSI + "?25l"
SHOW_CURSOR = CSI + "?25h"
CLEAR = CSI + "2J"

def get_size():
    cols, rows = shutil.get_terminal_size((80, 24))
    return rows - 1, cols  # leave last line for prompt

def render(matrix, ages, rows, cols):
    out_lines = []
    for r in range(rows):
        line = []
        for c in range(cols):
            ch = matrix[r][c]
            age = ages[r][c]
            if ch == " " or age is None:
                line.append(" ")
            else:
                # Age 0 = head (bright white), small ages = bright green, larger = dim green
                if age == 0:
                    line.append(f"{BRIGHT}{ch}{RESET}")
                elif age < 3:
                    line.append(f"{GREEN}{ch}{RESET}")
                else:
                    # dim green achieved by using darker ANSI (use 32 with 2m is fine)
                    line.append(f"{CSI}2;32m{ch}{RESET}")
        out_lines.append("".join(line))
    return "\n".join(out_lines)

def main():
    rows, cols = get_size()
    matrix = [[" "] * cols for _ in range(rows)]
    ages = [[None] * cols for _ in range(rows)]
    heads = [-1] * cols
    tails = [0] * cols
    tail_len = [0] * cols

    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.write(CLEAR)
    sys.stdout.flush()
    try:
        while True:
            # adapt if terminal resized
            r2, c2 = get_size()
            if r2 != rows or c2 != cols:
                rows, cols = r2, c2
                matrix = [[" "] * cols for _ in range(rows)]
                ages = [[None] * cols for _ in range(rows)]
                heads = [-1] * cols
                tails = [0] * cols
                tail_len = [0] * cols
                sys.stdout.write(CLEAR)

            # advance drops
            for c in range(cols):
                # maybe spawn
                if heads[c] == -1 and random.random() < DENSITY:
                    heads[c] = 0
                    tail_len[c] = random.randint(MIN_TAIL, MAX_TAIL)
                if heads[c] != -1:
                    h = heads[c]
                    if 0 <= h < rows:
                        ch = random.choice(CHARS)
                        matrix[h][c] = ch
                        ages[h][c] = 0
                    # increment all ages in this column (so trail fades)
                    # ages grow elsewhere too below
                    heads[c] += 1
                    # stop when head past tail end
                    if heads[c] - tail_len[c] >= rows:
                        heads[c] = -1

            # age everything and blank out too-old chars
            for r in range(rows):
                for c in range(cols):
                    if ages[r][c] is not None:
                        ages[r][c] += 1
                        if ages[r][c] > tail_len[c] + 4:
                            ages[r][c] = None
                            matrix[r][c] = " "

            # render
            sys.stdout.write(CSI + "H")  # move cursor to home
            sys.stdout.write(render(matrix, ages, rows, cols))
            sys.stdout.write(RESET)
            sys.stdout.flush()

            time.sleep(1.0 / FPS)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()