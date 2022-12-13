from helpers.functions import read_file_lines


if __name__ == "__main__":
    lines = read_file_lines("input")
    highest_calorie: int = 0
    cur_calorie: int = 0
    for line in lines:
        try:
            cur_calorie += int(line)
        except ValueError:
            highest_calorie = max(highest_calorie, cur_calorie)
            cur_calorie = 0
    print(highest_calorie)
