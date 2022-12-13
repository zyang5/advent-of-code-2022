from typing import List, AnyStr


def read_file_lines(filename: str) -> List[AnyStr]:
    with open(filename, "r") as input_file:
        lines = input_file.read().splitlines()

        input_file.close()
    return lines
