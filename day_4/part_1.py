from typing import Tuple

from helpers.functions import read_file_lines


def parse_line(raw_line: str) -> (Tuple[int, int], Tuple[int, int]):
    split_line = raw_line.split(",")
    first_parsed = split_line[0].split("-")
    second_parsed = split_line[1].split("-")
    return (int(first_parsed[0]), int(first_parsed[1])), (int(second_parsed[0]), int(second_parsed[1]))


if __name__ == "__main__":
    lines = read_file_lines("input")
    counter = 0
    for line in lines:
        pair1, pair2 = parse_line(line)
        if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
            counter += 1
        elif pair2[0] >= pair1[0] and pair2[1] <= pair1[1]:
            counter += 1
    print(counter)
