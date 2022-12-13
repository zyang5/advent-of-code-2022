from helpers.functions import read_file_lines


if __name__ == "__main__":
    lines = read_file_lines("input")
    result_sum = 0

    curr_lines = []
    for line in lines:
        curr_lines.append(set(line))
        if len(curr_lines) == 3:
            prio_letter = curr_lines[0].intersection(curr_lines[1]).intersection(curr_lines[2]).pop()
            result_sum += ord(prio_letter)
            result_sum -= 38 if prio_letter.isupper() else 96
            curr_lines = []
    print(result_sum)
