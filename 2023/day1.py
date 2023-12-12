import re


def add_digits(line):
    first_digit = re.search(r"\d", line)
    last_digit = re.search(r"\d(?=[^\d]*$)", line)
    return int(first_digit.group() + last_digit.group())


def part_1(lines):
    answer = 0
    for line in lines:
        answer += add_digits(line)
    return answer


def part_2(lines):
    answer = 0
    digits = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in lines:
        p = sorted([[line.find(d), d] for d in digits.keys() if line.find(d) != -1])

        line = line.replace(p[0][1], digits[p[0][1]]) if len(p) > 0 else line
        line = line.replace(p[-1][1], digits[p[-1][1]]) if len(p) > 1 else line
        answer += add_digits(line)

    return answer


def solve(lines):
    print(part_1(lines))
    print(part_2(lines))
