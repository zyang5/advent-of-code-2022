from helpers.functions import read_file_lines


if __name__ == "__main__":
    lines = read_file_lines("input")

    result_sum = 0
    for line in lines:
        half = int(len(line)/2)
        first_half = set(line[:half])
        for letter in line[half:]:
            if letter in first_half:
                result_sum += ord(letter)
                result_sum -= 38 if letter.isupper() else 96
                break
    print(result_sum)
