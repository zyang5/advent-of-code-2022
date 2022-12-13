from helpers.functions import read_file_lines
from part_1 import parse_crates, parse_move_line

if __name__ == "__main__":
    lines = read_file_lines("input")
    stacks = parse_crates(lines[:8])
    for line in lines[10:]:
        amount, stack_from, stack_to = parse_move_line(line)
        move_stack = stacks[stack_from-1][-amount:]
        stacks[stack_from-1] = stacks[stack_from-1][:-amount]
        stacks[stack_to-1] += move_stack

    result = ""
    for stack in stacks:
        result += stack[-1]
    print(result)
