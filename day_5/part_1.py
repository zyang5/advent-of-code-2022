from typing import List, Tuple

from helpers.functions import read_file_lines


def parse_crates(raw_lines: List[str]) -> List[List[str]]:
    crate_stacks: List[List] = [[] for _ in range(9)]
    raw_lines.reverse()
    for raw_line in raw_lines:
        stripped_line = raw_line.replace("[", "").replace("]", "")
        stripped_line = stripped_line.replace("   ", "")
        crates = stripped_line.split(" ")
        print(crates)
        for i, crate in enumerate(crates):
            if not crate:
                continue
            crate_stacks[i].append(crate)
    return crate_stacks


def parse_move_line(raw_line: str) -> Tuple[int, int, int]:
    split_line = raw_line.split(" ")
    return int(split_line[1]), int(split_line[3]), int(split_line[5])


if __name__ == "__main__":
    lines = read_file_lines("input")
    stacks = parse_crates(lines[:8])
    for line in lines[10:]:
        amount, stack_from, stack_to = parse_move_line(line)
        for _ in range(amount):
            stacks[stack_to-1].append(stacks[stack_from-1].pop())

    result = ""
    for stack in stacks:
        result += stack[-1]
    print(result)