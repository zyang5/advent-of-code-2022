from helpers.functions import read_file_lines
from day_4.part_1 import parse_line


if __name__ == "__main__":
    lines = read_file_lines("input")
    counter = 0
    for line in lines:
        pair1, pair2 = parse_line(line)
        if pair2[0] <= pair1[0] <= pair2[1]:
            counter += 1
        elif pair2[0] <= pair1[1] <= pair2[1]:
            counter += 1
        elif pair1[0] <= pair2[0] <= pair1[1]:
            counter += 1
    print(counter)
