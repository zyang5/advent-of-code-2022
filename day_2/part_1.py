from typing import Dict, Tuple

from helpers.functions import read_file_lines

WIN_LOSE_DRAW: Dict[Tuple, int] = {
    # WIN
    ("A", "Y"): 8,
    ("B", "Z"): 9,
    ("C", "X"): 7,
    # DRAW
    ("A", "X"): 4,
    ("B", "Y"): 5,
    ("C", "Z"): 6,
    # LOSE
    ("A", "Z"): 3,
    ("B", "X"): 1,
    ("C", "Y"): 2,
}


def parse_line(raw_line: str) -> (str, str):
    parsed = raw_line.split(" ")
    return parsed[0], parsed[1]


if __name__ == "__main__":
    lines = read_file_lines("input")
    total_score: int = 0
    for line in lines:
        parsed_line = parse_line(line)
        total_score += WIN_LOSE_DRAW[parsed_line]
    print(total_score)

