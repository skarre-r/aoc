"""
Part 1:
For each line, combine the first digit and the last digit (in that order) to form a single two-digit number.
The answer is the sum of all of these two-digit numbers.

Part 2:
Also include digits spelled out with letters. ("one", "two", etc...)
"""

from __future__ import annotations

import re


def solve_part_1(lines: list[str]) -> int:
    two_digit_numbers: list[int] = []
    for line in lines:
        line_numbers: list[str] = re.findall(pattern=r"\d+", string=line)
        if line_numbers:  # unnecessary
            two_digit_numbers.append(int(line_numbers[0][0] + line_numbers[-1][-1]))
    return sum(two_digit_numbers)


digit_map: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def solve_part_2(lines: list[str]) -> int:
    two_digit_numbers: list[int] = []
    for line in lines:
        # ?= is a "lookahead assertion": handles cases with overlapping digit strings, e.g. "twone"
        line_digits: list[str] = re.findall(
            pattern=r"(?=(one|two|three|four|five|six|seven|eight|nine|\d+))", string=line
        )
        if line_digits:
            first_digit: str = digit_map.get(line_digits[0], line_digits[0][0])
            last_digit: str = digit_map.get(line_digits[-1], line_digits[-1][-1])
            two_digit_numbers.append(int(first_digit + last_digit))
    return sum(two_digit_numbers)


def main() -> None:
    with open(file="day1.txt", mode="r", newline="\n") as input_file:
        lines: list[str] = [l for line in input_file.readlines() if (l := line.strip())]
    part_1_answer: int = solve_part_1(lines)
    print(f"{part_1_answer=}")
    part_2_answer: int = solve_part_2(lines)
    print(f"{part_2_answer=}")


if __name__ == "__main__":
    main()
