import argparse
from collections import Counter

def main(filename: str):

    with open(filename, "r") as file:
        lines: list[list[int]] = [list(map(int, line.strip().split())) for line in file.readlines()]

    l1: list[int] = []
    l2: list[int] = []

    for i in lines:
        l1.append(i[0])
        l2.append(i[1])

    l1.sort(); l2.sort()
    answer1: int = 0
    for i in range(len(l1)):
        answer1 += abs(l1[i] - l2[i])
    print(f"Answer 1: {answer1}")

    answer2: int = 0
    counter = Counter(l2)
    for i in range(len(l1)):
        answer2 += l1[i] * counter[l1[i]]
    print(f"Answer 2: {answer2}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename")
    args = parser.parse_args()

    main(args.input_filename)
