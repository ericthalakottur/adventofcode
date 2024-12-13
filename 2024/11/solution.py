import argparse
from collections import defaultdict

memory: dict[str, list[int]] = defaultdict(list)
TOTAL_TIMES = -1

def solve(val: str, level: int) -> int:
    global memory
    if val not in memory:
        memory[val] = [-1] * (TOTAL_TIMES + 1)

    if memory[val][level] != -1:
        return memory[val][level]

    if level == 0:
        memory[val][level] = 1
    elif val == "0":
        memory[val][level] = solve("1", level - 1)
    elif len(val) % 2 == 0:
        n: int = len(val)
        memory[val][level] = solve(str(int(val[:n//2])), level - 1) + solve(str(int(val[n//2:])), level - 1)
    else:
        memory[val][level] = solve(str(int(val) * 2024), level - 1)
    return memory[val][level]


def main(filename: str):
    with open(filename, "r") as file:
        ip: list[str] = file.readline().split()

    answer: int = 0
    for val in ip:
        answer += solve(val, TOTAL_TIMES)

    print(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename")
    parser.add_argument("times")
    args = parser.parse_args()

    TOTAL_TIMES = int(args.times)

    main(args.input_filename)
