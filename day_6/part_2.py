from helpers.functions import read_file_lines


if __name__ == "__main__":
    lines = read_file_lines("input")
    marker = set()
    i = 0
    while len(marker) < 14:
        marker = set(lines[0][i:i+14])
        i += 1
    print(marker)
    print(i+13)
