import heapq
from typing import List

from helpers.functions import read_file_lines


if __name__ == "__main__":
    lines = read_file_lines("input")

    top_three: List[int] = []
    cur_calorie: int = 0
    for line in lines:
        try:
            cur_calorie += int(line)
        except ValueError:
            if len(top_three) < 3:
                heapq.heappush(top_three, cur_calorie)
                cur_calorie = 0
                continue
            heapq.heappushpop(top_three, cur_calorie)
            cur_calorie = 0
    print(sum(top_three))

