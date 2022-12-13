from typing import Dict, Tuple

from helpers.functions import read_file_lines
from day_2.part_1 import parse_line

WIN_LOSE_DRAW: Dict[Tuple, int] = {
    # WIN
    ("A", "Z"): 8,
    ("B", "Z"): 9,
    ("C", "Z"): 7,
    # DRAW
    ("A", "Y"): 4,
    ("B", "Y"): 5,
    ("C", "Y"): 6,
    # LOSE
    ("A", "X"): 3,
    ("B", "X"): 1,
    ("C", "X"): 2,
}


if __name__ == "__main__":
    lines = read_file_lines("input")
    total_score: int = 0
    for line in lines:
        parsed_line = parse_line(line)
        total_score += WIN_LOSE_DRAW[parsed_line]
    print(total_score)

