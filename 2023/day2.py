import re


def part_1(lines):
    color_count = {"red": 12, "green": 13, "blue": 14}
    answer = 0
    for line in lines:
        valid = False
        game_id = int(re.search(r"Game (\d+):", line).group(1))
        for color in color_count.keys():
            values = re.findall(r"\b(\d+) {}\b".format(color), line)
            valid = all(int(v) <= color_count[color] for v in values)
        if valid:
            answer += game_id
    return answer


def part_2(lines):
    answer = 0
    for line in lines:
        color_count = {"red": 0, "green": 0, "blue": 0}
        prod = 1
        for color in color_count.keys():
            values = [int(i) for i in re.findall(r"\b(\d+) {}\b".format(color), line)]
            prod = prod * sorted(values, reverse=True)[0]
        answer += prod
    return answer


def solve(lines):
    print(__file__.split("/")[-1], "part_1:", part_1(lines))
    print(__file__.split("/")[-1], "part_2:", part_2(lines))
